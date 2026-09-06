# Architecture

Text is cleaned/tokenized, passed through a text-to-semantic model, and decoded through DAC/audio components. The inference engine handles references and vector-quantized audio; WebUI/server layers expose the same model capabilities. The tokenizer has a tiktoken checkpoint path validated by a synthetic smoke, which is distinct from full S2 model inference.

Sources: `fish_speech/tokenizer.py`, `fish_speech/models`, `fish_speech/inference_engine`, `docs/en/inference.md`.
