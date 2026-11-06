---
max_turns: 6
timeout_seconds: 240
allowed_tools: [Skill, Read]
runs: 5
expected_outcome: The body is written as paragraphs. Two one-line changes do not become a bullet list.
---

Write a commit message for this change to a C command-line tool. Reply with only the commit message.

The change does two small things in main.c: the --verbose flag was documented in --help but never parsed, so it is now parsed; and the error message for a missing input file now names the file.
