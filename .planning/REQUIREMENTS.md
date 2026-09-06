# Requirements: soft-fish-speech

**Defined:** 2026-09-06
**Core Value:** Reproduce tokenizer and CLI readiness while keeping tokenizer evidence distinct from model inference.

## v1 Requirements

### No-Download Baseline

- [ ] **FISH-01**: Operator can run a repository-owned synthetic tiktoken encode/decode/save/restore check without downloading or loading a model.
- [ ] **FISH-02**: Operator can invoke supported package and CLI help or invalid-argument boundaries and observe deterministic model-free results.
- [ ] **FISH-03**: Operator can run one project verification command that distinguishes tokenizer passes, CLI passes, model-backed skips, and failures.

## v2 Requirements

### Model-Backed Runtime

- **FISH-04**: Operator can synthesize valid audio from an approved local S2 checkpoint.
- **FISH-05**: Operator can verify voice cloning, multilingual quality, WebUI, and server behavior on compatible hardware.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Automatic model downloads | Asset acquisition is operator-controlled. |
| Model-inference claims from tokenizer checks | Tokenization does not execute semantic generation or audio decoding. |
| Existing untracked package/test stubs | Intent and provenance are unresolved. |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| FISH-01 | Phase 1 | Pending |
| FISH-02 | Phase 1 | Pending |
| FISH-03 | Phase 1 | Pending |

**Coverage:** 3 total, 3 mapped, 0 unmapped ✓

---
*Requirements defined: 2026-09-06*
*Last updated: 2026-09-06 after brownfield initialization*
