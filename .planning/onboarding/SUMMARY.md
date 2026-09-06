# Brownfield onboarding summary

- Repository: `soft-fish-speech`
- Mode: fast brownfield onboarding
- Sources: canonical shared baseline, `GSD-BOOTSTRAP.md`, repository README/project goal, package metadata and inference docs
- Codebase map: fast map complete (`STACK.md`, `INTEGRATIONS.md`, `ARCHITECTURE.md`, `STRUCTURE.md`)
- Existing capabilities validated: tokenizer/model/DAC/inference/WebUI/server/docs surfaces are present; tiktoken support at commit `9c9633e` and synthetic tiktoken smoke are recorded; model inference is not claimed
- Active milestone: v1 local reproducible CLI/inference smoke baseline without model download
- Active requirements: FISH-01 through FISH-03 map to Phase 1
- Next action: discuss and plan the tokenizer and model-free CLI baseline
- Verification gap: no `scripts/verify`; no model download or S2 model inference performed
