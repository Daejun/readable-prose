---
type: llm
---

Look only at the commit message in the reply.
PASS if the four changes appear as a list, one change per item, and the line just before the list is a sentence that says what the changes are for or what they have in common (not only "Changes:" or "This patch:").
FAIL if the changes are not a list, or a list item holds more than one of the four changes, or the list has no such sentence before it.
