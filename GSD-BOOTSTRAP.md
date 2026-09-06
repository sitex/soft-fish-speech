---
document: gsd-brownfield-bootstrap
project: soft-fish-speech
git_root: /home/rocky/projects/soft-fish-speech
github_repository: sitex/soft-fish-speech
generated_at: 2026-09-06T02:03:45Z
thoughts_status: available
github_status: repository resolved; Issues API unavailable or disabled for this fork
include_personal: false
---

# Purpose

Vendor fork of Fish Audio S2 Pro providing multilingual TTS, voice cloning, CLI, WebUI, server, Docker and training/inference surfaces. [T1]

# Implemented Capabilities

- `fish_speech` contains tokenizer, text-to-semantic, DAC, inference engine, datasets and utilities. [T2]
- CLI, WebUI, server and Docker paths are documented. [T2]
- `tiktoken>=0.8.0` is declared and commit `9c9633e` added tiktoken checkpoint support. [T2]
- A synthetic tiktoken smoke has passed for the tokenizer/checkpoint path. [T1]

# Current Milestone

Active v1: local reproducible CLI/inference smoke baseline without model download. The synthetic tiktoken smoke does not prove model inference. [T1]

# Open Requirements

- Validate the no-download CLI/inference boundary smoke. [T1]
- Later validate S2 model inference, audio generation, WebUI, server and multilingual quality separately. [T1]

# Accepted Decisions

- Preserve the tiktoken support and synthetic smoke as evidence, but do not generalize it to model inference. [T1]
- Treat this as a vendor fork and preserve upstream boundary. [T1]
- Do not download models during onboarding. [T1]

# Constraints

- Python >=3.10, PyTorch 2.8.0, substantial GPU memory and external checkpoints for real inference. [T1]
- Fish Audio Research License applies. [T1]
- Existing untracked `src/` and `tests/` are out of scope and must remain unchanged. [T2]

# Unresolved Conflicts

None identified from available sources.

# Source Thoughts

- T1: `/home/rocky/thoughts/repos/soft-fish-speech/shared/research/2026-09-06-project-baseline.md`
- T2: `/home/rocky/projects/soft-fish-speech/README.md`, `PROJECT_GOAL.md`, `pyproject.toml`, `docs/en/inference.md`

# Source Issues

None included; the Issues API is unavailable or disabled for this fork.

# Source Limitations

No model download or model inference was performed; synthetic tiktoken smoke is the only stated completed smoke evidence.
