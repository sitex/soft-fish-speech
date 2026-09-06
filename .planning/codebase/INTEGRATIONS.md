# Integrations

- Hugging Face/model checkpoints and documented Docker workflows are external runtime boundaries.
- CLI inference uses DAC and text-to-semantic scripts; WebUI and API/server surfaces are documented.
- `tiktoken>=0.8.0` supports model checkpoints; commit `9c9633e` introduced that support.
- Upstream reference is `fishaudio/fish-speech`; this repository is the `sitex/soft-fish-speech` vendor mirror.

Sources: `docs/en/inference.md`, `docs/en/server.md`, `pyproject.toml`, `git show 9c9633e`.
