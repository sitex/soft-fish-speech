# soft-fish-speech

## What This Is

`soft-fish-speech` is the personal `sitex` fork of Fish Speech S2 Pro for local multilingual TTS and voice-cloning integration work. The repository includes tokenizer, text-to-semantic, codec, CLI, WebUI, server, Docker, and training surfaces; local verification begins with no-download boundaries.

## Core Value

The operator can reproduce tokenizer and CLI readiness checks while keeping tokenizer evidence distinct from model-inference claims.

## Requirements

### Validated

- ✓ Tokenizer, text-to-semantic, DAC, inference engine, CLI, WebUI, server, Docker, and multilingual documentation surfaces exist — existing repository
- ✓ Commit `9c9633e` adds tiktoken checkpoint support and passed one synthetic encode/decode/save/restore smoke — local evidence
- ✓ The personal fork publishes portfolio work separately from the Fish Audio `upstream` remote — onboarding

### Active

- [ ] Convert the synthetic tiktoken smoke into a reproducible repository check.
- [ ] Run supported model-free package and CLI help or argument-validation boundaries without downloading weights.
- [ ] Add one project verification command that separates tokenizer passes, model-free CLI passes, and model-backed skips.

### Out of Scope

- Downloading S2 checkpoints during onboarding — asset acquisition is operator-controlled.
- Claiming speech generation, voice-cloning quality, multilingual quality, or server readiness from tokenizer-only evidence.
- Committing existing untracked package/test stubs — their intent and provenance are unresolved.

## Context

The fork originates from `fishaudio/fish-speech`. A divergent local commit and tiktoken implementation were preserved on `origin/portfolio` without rewriting upstream history. The synthetic smoke used the existing project environment and no model. Source-linked evidence lives in `GSD-BOOTSTRAP.md`, `.planning/codebase/`, and canonical HumanLayer Thoughts.

## Constraints

- **Runtime**: Python 3.10+, PyTorch 2.8, audio tooling, and external checkpoints — environment creation can require system packages.
- **Licensing**: the Fish Audio Research License and separate model terms constrain redistribution and use.
- **Assets**: model weights remain external — no model-backed check is implied by tokenizer success.
- **Verification**: no `scripts/verify` exists — Phase 1 must add a deterministic no-download gate.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Preserve the tiktoken implementation as a separate commit | Keep personal functionality reviewable from vendor history | ✓ Good |
| Treat the synthetic tokenizer smoke as narrow evidence | It does not load a model or synthesize audio | ✓ Good |
| Keep untracked package/test stubs out of onboarding | Their ownership and expected behavior are unresolved | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition**:
1. Move verified no-download requirements to Validated with evidence.
2. Preserve the boundary between tokenizer, CLI, and model-inference claims.
3. Record new licensing, asset, and hardware constraints.
4. Recheck the maintained-fork description and core value.

**After each milestone**:
1. Review requirement and model-asset status.
2. Reconfirm the upstream/fork boundary.
3. Define the next evidence-backed milestone.

---
*Last updated: 2026-09-06 after brownfield initialization*
