# Structure

- `fish_speech/text`, `tokenizer.py`, `content_sequence.py`: text and token boundaries.
- `fish_speech/models/text2semantic`: semantic generation; `fish_speech/models/dac`: audio codec.
- `fish_speech/inference_engine`: reference loading, VQ management and inference utilities.
- `tools/server`, `tools/webui`, `awesome_webui`: serving and UI surfaces.
- `docs/{en,zh,ja,ko,pt,es,ar}`: multilingual user documentation; `docker`: deployment material.
- Existing untracked `src/` and `tests/` remain untouched.

Sources: repository tree and `README.md`.
