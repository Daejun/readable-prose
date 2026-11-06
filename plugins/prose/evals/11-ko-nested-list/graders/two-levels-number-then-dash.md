---
type: regex
pattern: '^\d+[.)] [^\n]*\n(?:[ \t]+[^\n]*\n|[ \t]*\n)*?[ \t]+[-*] '
flags: m
match: contains
target: last_message
---
