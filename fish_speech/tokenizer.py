import base64
import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING, List, Union

import torch
from transformers import AutoTokenizer

if TYPE_CHECKING:
    from transformers import PreTrainedTokenizerFast

logger = logging.getLogger(__name__)

# Constants definitions
EOS_TOKEN = "<|endoftext|>"
PAD_TOKEN = "<|pad|>"
IM_START_TOKEN = "<|im_start|>"
IM_END_TOKEN = "<|im_end|>"
PHONEME_START_TOKEN = "<|phoneme_start|>"
PHONEME_END_TOKEN = "<|phoneme_end|>"

MODALITY_TEXT_TOKEN = "<|text|>"
MODALITY_VOICE_TOKEN = "<|voice|>"
MODALITY_INTERLEAVE_TOKEN = "<|interleave|>"
AUDIO_START_TOKEN = "<|audio_start|>"
AUDIO_END_TOKEN = "<|audio_end|>"
AUDIO_EMBED_TOKEN = "<|audio_pad|>"

MODALITY_TOKENS = {
    "text": MODALITY_TEXT_TOKEN,
    "voice": MODALITY_VOICE_TOKEN,
    "interleave": MODALITY_INTERLEAVE_TOKEN,
}

SEMANTIC_TOKEN_TEMPLATE = "<|semantic:{i}|>"
SEMANTIC_TOKENS = [SEMANTIC_TOKEN_TEMPLATE.format(i=i) for i in range(4096)]

ALL_SPECIAL_TOKENS = [
    EOS_TOKEN,
    PAD_TOKEN,
    IM_START_TOKEN,
    IM_END_TOKEN,
    PHONEME_START_TOKEN,
    PHONEME_END_TOKEN,
    MODALITY_TEXT_TOKEN,
    MODALITY_VOICE_TOKEN,
    MODALITY_INTERLEAVE_TOKEN,
    AUDIO_START_TOKEN,
    AUDIO_END_TOKEN,
    AUDIO_EMBED_TOKEN,
    *SEMANTIC_TOKENS,
]

# GPT-4o-derived split pattern shipped with the OpenAudio/Fish-Speech tiktoken
# tokenizer (e.g. openaudio-s1-mini). Copied VERBATIM from fish-speech v1.5.0 —
# including the `(\?!\S)` quirk (an upstream typo for the `(?!\S)` negative
# lookahead). The model was trained with this exact pattern, so it must be
# reproduced byte-for-byte; "fixing" it would change tokenization and corrupt
# audio. Used only by the tiktoken backend below.
FISH_TIKTOKEN_PATTERN = "|".join(
    [
        r"(?i:'s|'t|'re|'ve|'m|'ll|'d)",
        r"\p{P}",
        r"[^\r\n\p{L}\p{N}]?\p{L}+",
        r"\p{N}",
        r" ?[^\s\p{L}\p{N}]+[\r\n]*",
        r"\s*[\r\n]+",
        r"\s+(\?!\S)",
        r"\s+",
    ]
)
TIKTOKEN_MAX_ENCODE_CHARS = 400_000


class FishTokenizer:
    """Unified tokenizer wrapper with two backends:

    - "tiktoken": for OpenAudio S1 / s1-mini checkpoints that ship
      `tokenizer.tiktoken` (+ optional `special_tokens.json`). The current
      `transformers` cannot load these via AutoTokenizer (no HF tokenizer.json;
      it falls back to the model config and rejects `dual_ar`), so we build a
      `tiktoken.Encoding` directly.
    - "hf": AutoTokenizer for newer S2 checkpoints that ship an HF tokenizer.

    The public surface used by the inference pipeline is small:
    `encode`, `decode`, `get_token_id`, `semantic_begin_id`, `semantic_end_id`.
    """

    def __init__(self, model_path: str):
        path = Path(model_path)
        tiktoken_file = (path / "tokenizer.tiktoken") if path.is_dir() else path

        if str(tiktoken_file).endswith(".tiktoken") and tiktoken_file.exists():
            self.backend = "tiktoken"
            self._tokenizer = None
            self._init_tiktoken(tiktoken_file)
        else:
            self.backend = "hf"
            self._tokenizer = AutoTokenizer.from_pretrained(model_path)
            self._vocab = self._tokenizer.get_vocab()

        self._init_semantic_range()

        logger.info(
            f"Loaded {self.backend} tokenizer. Semantic Range: "
            f"{self.semantic_begin_id} -> {self.semantic_end_id}"
        )

    # --- tiktoken backend ----------------------------------------------------
    @staticmethod
    def load_tiktoken_bpe(tiktoken_bpe_file) -> dict[bytes, int]:
        data: dict[bytes, int] = {}
        for line in Path(tiktoken_bpe_file).read_text().splitlines():
            if not line:
                continue
            token, rank = line.split()
            data[base64.b64decode(token)] = int(rank)
        return data

    def _init_tiktoken(self, tiktoken_file: Path):
        import tiktoken

        mergeable_ranks = self.load_tiktoken_bpe(tiktoken_file)

        # Prefer the checkpoint's explicit special-token map (s1-mini and newer
        # ship `special_tokens.json` with fixed IDs). Fall back to deriving
        # sequential IDs from ALL_SPECIAL_TOKENS for older packs that omit it.
        st_path = tiktoken_file.parent / "special_tokens.json"
        if st_path.exists():
            raw = json.loads(st_path.read_text())
            self.all_special_tokens_with_ids = {k: int(v) for k, v in raw.items()}
        else:
            begin = len(mergeable_ranks)
            self.all_special_tokens_with_ids = {
                tok: begin + i for i, tok in enumerate(ALL_SPECIAL_TOKENS)
            }

        self.tkt_model = tiktoken.core.Encoding(
            name=tiktoken_file.stem,
            pat_str=FISH_TIKTOKEN_PATTERN,
            mergeable_ranks=mergeable_ranks,
            special_tokens=self.all_special_tokens_with_ids,
        )
        self._vocab = dict(self.all_special_tokens_with_ids)

    def _init_semantic_range(self):
        """Locate the contiguous <|semantic:i|> id block.

        Inference adds raw codebook indices to `semantic_begin_id`
        (content_sequence.py: `code + semantic_begin_id`), so these ids must be
        contiguous and ordered — verified true for s1-mini (151658..155753).
        """
        valid_ids: list[int] = []
        self.semantic_id_to_token_id: dict[int, int] = {}
        for code_idx in range(4096):
            token = SEMANTIC_TOKEN_TEMPLATE.format(i=code_idx)
            token_id = self._vocab.get(token)
            if token_id is not None:
                self.semantic_id_to_token_id[code_idx] = token_id
                valid_ids.append(token_id)

        if valid_ids:
            self.semantic_begin_id = min(valid_ids)
            self.semantic_end_id = max(valid_ids)
        else:
            logger.error(
                "CRITICAL ERROR: No semantic tokens found in vocab! "
                "Audio cannot be synthesized."
            )
            self.semantic_begin_id = 0
            self.semantic_end_id = 0

        self.semantic_map_tensor = torch.zeros(4096, dtype=torch.long)
        for k, v in self.semantic_id_to_token_id.items():
            self.semantic_map_tensor[k] = v

    # --- public surface ------------------------------------------------------
    @property
    def vocab_size(self):
        if self.backend == "tiktoken":
            return self.tkt_model.n_vocab
        return self._tokenizer.vocab_size

    @property
    def pad_token_id(self):
        if self.backend == "tiktoken":
            return self.all_special_tokens_with_ids.get(PAD_TOKEN)
        return self._tokenizer.pad_token_id

    @property
    def eos_token_id(self):
        if self.backend == "tiktoken":
            return self.all_special_tokens_with_ids.get(
                "<|end_of_text|>"
            ) or self.all_special_tokens_with_ids.get(EOS_TOKEN)
        return self._tokenizer.eos_token_id

    def get_token_id(self, token: str) -> int:
        if self.backend == "tiktoken":
            return self.all_special_tokens_with_ids[token]
        return self._tokenizer.convert_tokens_to_ids(token)

    def encode(
        self, text: str, add_special_tokens: bool = False, **kwargs
    ) -> List[int]:
        if self.backend == "tiktoken":
            # `add_special_tokens` is HF-only; for tiktoken we always allow the
            # literal <|...|> markers in the text to map to their special ids
            # (the conversation template embeds <|im_start|>, <|text|>, etc.).
            allowed = self.tkt_model.special_tokens_set
            chunks = [
                text[i : i + TIKTOKEN_MAX_ENCODE_CHARS]
                for i in range(0, max(len(text), 1), TIKTOKEN_MAX_ENCODE_CHARS)
            ]
            out: List[int] = []
            for chunk in chunks:
                out.extend(
                    self.tkt_model.encode(
                        chunk, allowed_special=allowed, disallowed_special=set()
                    )
                )
            return out

        # [FIX] Force Qwen/Tiktoken HF backends to parse special tokens inline
        import inspect

        sig = inspect.signature(self._tokenizer.encode)
        if "allowed_special" in sig.parameters and "allowed_special" not in kwargs:
            kwargs["allowed_special"] = "all"
        return self._tokenizer.encode(
            text, add_special_tokens=add_special_tokens, **kwargs
        )

    def decode(self, tokens: Union[List[int], int], **kwargs) -> str:
        if self.backend == "tiktoken":
            if isinstance(tokens, int):
                tokens = [tokens]
            return self.tkt_model.decode(list(tokens))
        return self._tokenizer.decode(tokens, **kwargs)

    def save_pretrained(self, path: str):
        if self.backend == "tiktoken":
            out = Path(path)
            out.mkdir(parents=True, exist_ok=True)
            with open(out / "tokenizer.tiktoken", "w") as f:
                for token, rank in self.tkt_model._mergeable_ranks.items():
                    f.write(f"{base64.b64encode(token).decode()} {rank}\n")
            with open(out / "special_tokens.json", "w") as f:
                json.dump(
                    self.all_special_tokens_with_ids, f, indent=2, ensure_ascii=False
                )
            return
        self._tokenizer.save_pretrained(path)

    @classmethod
    def from_pretrained(cls, path: str):
        return cls(path)

    def __getattr__(self, name):
        # Delegate unknown attributes to the HF backend only. For the tiktoken
        # backend there is no underlying HF object, so surface a clear error.
        tk = self.__dict__.get("_tokenizer")
        if tk is not None:
            return getattr(tk, name)
        raise AttributeError(name)
