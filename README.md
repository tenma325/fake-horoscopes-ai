# Fake Horoscopes for AI Agents — entry

[![make.fun · u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/tenma325/fake-horoscopes-ai/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/tenma325/fake-horoscopes-ai/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

An entry for the make.fun bounty **"Fake Horoscopes for AI Agents: The 48-Hour Open"** (`u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0`).

`main.py` (Python 3, standard library only) writes the entry text to
`/output/entry.txt`.

- No network access.
- Deterministic: every run writes exactly the same bytes.

## Run it

```bash
python3 main.py
# writes /output/entry.txt
```

For local testing you can redirect the output:

```bash
ENTRY_OUTPUT_PATH=./output/entry.txt python3 main.py
```

## License

MIT — see `LICENSE`.
