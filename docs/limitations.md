# Limitations

- BBQ targets social biases attested in U.S. English-speaking contexts.
- Model behavior can depend on prompt, decoding, runtime, and quantization.
- Per-example raw outputs were not retained in the supplied files for Granite 4.1 3B, Phi-4 Mini 3.8B, and Ministral 3 3B; their verified summary exports are used.
- The exact inference prompt/runtime for GPT 5.5 and GPT 5.6 Luna is unavailable in the supplied artifacts.
- The two GPT high-condition answer files are identical and perfectly match the gold sequence; this is reported transparently rather than explained without evidence.
- Qwen3 4B has 49 strict-format invalid outputs and therefore less than 100% output coverage.
