---
type: regex
pattern: '^\d+[.)] [^\n]*\n(?:[ \t]+[^\n]*\n|[ \t]*\n)*?[ \t]+\d+[.)] '
flags: m
match: not_contains
target: last_message
---
