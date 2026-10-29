---
max_turns: 6
timeout_seconds: 240
allowed_tools: [Skill, Read]
runs: 3
---

아래 변경으로 PR 본문을 써 주세요. 바로 올릴 거예요.

변경: src/cache.c에서 evict_entry()가 refcount를 내리기 전에 list에서 빼도록 순서를 바꿈. 이전에는 동시에 lookup이 들어오면 해제된 entry를 볼 수 있었음. stress test 100회에서 crash 7회 → 0회.
