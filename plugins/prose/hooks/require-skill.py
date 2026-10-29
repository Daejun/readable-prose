#!/usr/bin/env python3
"""PreToolUse gate: a Bash command that posts to GitHub is denied until the
prose:readable skill has run in the current turn.

Set READABLE_PROSE_GATE=0 to turn the gate off. Any error lets the command
through.
"""
import json
import os
import re
import sys

POSTING = [
    re.compile(r"\bgh\s+(pr|issue)\s+(create|comment)\b"),
    re.compile(r"\bgh\s+pr\s+review\b[^|;&\n]*(\s-b\b|\s--body)"),
    re.compile(r"\bgh\s+(pr|issue)\s+edit\b[^|;&\n]*(\s-b\b|\s--body)"),
    # gh api writes to comments or reviews only when it sends fields or a body
    re.compile(r"\bgh\s+api\b(?=[^|;&\n]*/(comments|reviews)\b)"
               r"(?=[^|;&\n]*(\s-[fF]\b|\s--(raw-)?field\b|\s--input\b))"),
]

SKILL_NAMES = ("prose:readable", "readable")
SLASH = re.compile(r"<command-name>/(prose:)?readable</command-name>")

REASON = (
    "prose: 이 명령은 GitHub에 글을 올립니다. "
    "prose:readable skill을 먼저 불러 글을 고치고 "
    "원문과 사실을 대조한 뒤 같은 명령을 다시 실행하세요. "
    "이 turn에서 skill을 한 번 부르면 이후 명령은 막지 않습니다."
)


def is_user_prompt(entry):
    if entry.get("type") != "user" or entry.get("isMeta"):
        return False
    content = entry.get("message", {}).get("content")
    if isinstance(content, str):
        return True
    if isinstance(content, list):
        return not any(c.get("type") == "tool_result" for c in content)
    return False


def prompt_text(entry):
    content = entry["message"]["content"]
    if isinstance(content, str):
        return content
    return " ".join(c.get("text", "") for c in content)


def skill_ran_this_turn(transcript_path):
    entries = []
    with open(transcript_path, encoding="utf-8") as f:
        for line in f:
            try:
                entries.append(json.loads(line))
            except ValueError:
                continue
    for entry in reversed(entries):
        if entry.get("type") == "assistant":
            for c in entry.get("message", {}).get("content", []):
                if (c.get("type") == "tool_use" and c.get("name") == "Skill"
                        and str(c.get("input", {}).get("skill", "")) in SKILL_NAMES):
                    return True
        elif is_user_prompt(entry):
            # /prose:readable typed by the user also counts
            return bool(SLASH.search(prompt_text(entry)))
    return False


def main():
    if os.environ.get("READABLE_PROSE_GATE") == "0":
        return
    data = json.load(sys.stdin)
    if data.get("tool_name") != "Bash":
        return
    command = data.get("tool_input", {}).get("command", "")
    if not any(p.search(command) for p in POSTING):
        return
    if skill_ran_this_turn(data["transcript_path"]):
        return
    json.dump({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": REASON,
    }}, sys.stdout, ensure_ascii=False)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
