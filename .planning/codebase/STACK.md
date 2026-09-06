# Stack

- Python >=3.10 package built with setuptools and managed by `pyproject.toml`/`uv.lock`.
- PyTorch 2.8.0, torchaudio, Transformers, Lightning, Gradio, Uvicorn and tiktoken.
- Package code lives in `fish_speech`; local untracked `src/` and `tests/` are preserved and not part of this onboarding change.
- Real S2 inference is GPU/checkpoint dependent; no model is downloaded here.

Sources: `pyproject.toml`, `docs/en/install.md`, repository tree.
