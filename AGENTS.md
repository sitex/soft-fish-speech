<!-- GSD:project-start source:PROJECT.md -->

## Project

**soft-fish-speech**

`soft-fish-speech` is the personal `sitex` fork of Fish Speech S2 Pro for local multilingual TTS and voice-cloning integration work. The repository includes tokenizer, text-to-semantic, codec, CLI, WebUI, server, Docker, and training surfaces; local verification begins with no-download boundaries.

**Core Value:** The operator can reproduce tokenizer and CLI readiness checks while keeping tokenizer evidence distinct from model-inference claims.

### Constraints

- **Runtime**: Python 3.10+, PyTorch 2.8, audio tooling, and external checkpoints — environment creation can require system packages.
- **Licensing**: the Fish Audio Research License and separate model terms constrain redistribution and use.
- **Assets**: model weights remain external — no model-backed check is implied by tokenizer success.
- **Verification**: no `scripts/verify` exists — Phase 1 must add a deterministic no-download gate.

<!-- GSD:project-end -->

<!-- GSD:stack-start source:codebase/STACK.md -->

## Technology Stack

- Python >=3.10 package built with setuptools and managed by `pyproject.toml`/`uv.lock`.
- PyTorch 2.8.0, torchaudio, Transformers, Lightning, Gradio, Uvicorn and tiktoken.
- Package code lives in `fish_speech`; local untracked `src/` and `tests/` are preserved and not part of this onboarding change.
- Real S2 inference is GPU/checkpoint dependent; no model is downloaded here.

<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->

## Conventions

Conventions not yet established. Will populate as patterns emerge during development.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->

## Architecture

# Architecture

Text is cleaned/tokenized, passed through a text-to-semantic model, and decoded through DAC/audio components. The inference engine handles references and vector-quantized audio; WebUI/server layers expose the same model capabilities. The tokenizer has a tiktoken checkpoint path validated by a synthetic smoke, which is distinct from full S2 model inference.

Sources: `fish_speech/tokenizer.py`, `fish_speech/models`, `fish_speech/inference_engine`, `docs/en/inference.md`.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->

## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.codex/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->

## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:

- `$gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `$gsd-debug` for investigation and bug fixing
- `$gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->

<!-- GSD:profile-start -->

## Developer Profile

> Profile not yet configured. Run `$gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
