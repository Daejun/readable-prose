---
max_turns: 6
timeout_seconds: 240
allowed_tools: [Skill, Read]
runs: 3
---

Write a commit message for this change: in parse_args(), the --timeout value was parsed with atoi(), so "10s" became 10 and "abc" became 0 silently. Now it uses strtol() and rejects trailing garbage with an error.
