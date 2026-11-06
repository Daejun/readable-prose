---
max_turns: 6
timeout_seconds: 240
allowed_tools: [Skill, Read]
runs: 5
expected_outcome: Four independent changes are listed, one per item, after a sentence that says what the list is for.
---

Write a commit message for this cleanup of a C library's buffer code. Reply with only the commit message.

The patch makes four independent changes in buf.c: buf_alloc() now returns NULL instead of aborting when malloc fails; buf_free() accepts a NULL pointer; buf_append() checks for size_t overflow before growing; and the unused helper buf_debug_dump() is removed.
