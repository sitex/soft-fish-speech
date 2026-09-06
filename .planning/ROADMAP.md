# Roadmap: soft-fish-speech

## Phases

- [ ] **Phase 1: Tokenizer and Model-Free CLI Baseline** - Turn the existing tokenizer smoke into a deterministic no-download project gate.

## Phase Details

### Phase 1: Tokenizer and Model-Free CLI Baseline
**Goal:** The operator can reproduce tiktoken and model-free CLI checks through one gate that never implies model inference.
**Mode:** mvp
**Depends on:** Nothing (first phase)
**Requirements:** FISH-01, FISH-02, FISH-03
**Success Criteria:**
1. A repository-owned test reproduces tiktoken encode, decode, special-token mapping, save, and restore without model assets.
2. Supported package and CLI help or invalid-argument paths return deterministic documented results without downloading weights.
3. The verification command runs the tokenizer and CLI checks and exits nonzero on a real failure.
4. Model loading, speech generation, cloning, WebUI, and server checks are visibly reported as skipped.
5. Existing untracked package/test stubs remain unchanged and outside the commit.
**Plans:** TBD

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Tokenizer and Model-Free CLI Baseline | 0/TBD | Not started | - |
