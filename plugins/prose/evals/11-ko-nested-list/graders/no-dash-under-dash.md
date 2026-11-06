---
type: regex
pattern: '^[-*] [^\n]*\n(?:[ \t]+[^\n]*\n|[ \t]*\n)*?[ \t]+[-*] '
flags: m
match: not_contains
target: last_message
---
