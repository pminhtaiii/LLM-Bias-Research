# GPT protocol information still required

Before the GPT results are promoted from `REPORTED_AGGREGATE` to independently verified/canonical:

- exact model/API identifiers
- exact system prompt
- exact user prompt/template
- reasoning-mode semantics for high / medium / low
- temperature / top_p / max output tokens / seed if applicable
- parser rule
- invalid / empty / truncated handling
- preferably raw per-example predictions or the notebook/script that produced the aggregate CSV

The current repository preserves the supplied aggregate results without inventing these missing details.
