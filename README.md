# readable-prose

A Claude Code plugin that makes model-written prose easier to read on the first pass. Rules are in Korean; they apply to Korean answers and to English commit messages, PR bodies and review replies.

Claude Code가 쓴 글을 처음 읽을 때 이해되게 만드는 plugin입니다.

## 설치

```
/plugin marketplace add Daejun/readable-prose
/plugin install readable-prose@readable-prose
```

GitHub SSH key가 없는 machine에서는 `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1`을 설정한 뒤 실행합니다.

## 들어 있는 것

| 구성 | 하는 일 | context 비용 |
|---|---|---|
| `SessionStart` hook | session 시작, `/clear`, compaction 때 쓰기 규칙 4줄(`hooks/writing-rules.md`)을 context에 넣습니다 | session마다 약 800자 |
| `readable-prose` skill | 글을 고쳐 쓸 때 구조를 바꾸고(결론 먼저, label 붙은 목록, 한 문장에 판정 하나) 원문과 대조해 사실을 지킵니다 | skill을 부를 때 약 3,300자 |

skill은 "읽기 쉽게", "AI 문체", "다듬어", "make this readable" 같은 요청이나 PR body, commit message, review 답글을 게시하기 전에 불립니다. 직접 부르려면 `/readable-prose:readable-prose`를 씁니다.

## 근거

- Clark, Martin, Mahowald (2026), "Why is AI-generated language so hard to understand?", arXiv:2610.29162. 근거는 정보 밀도 압력 때문에 model이 짧은 구문을 고른다는 분석입니다.
- 만든 사람이 직접 한 blind 비교 평가입니다. 비교한 판은 셋입니다.
  - 문장 단위 규칙(declauding 계열 포함)만 적용한 판
  - "사람이 읽기 쉽게 고쳐라"만 받은 판
  - 이 plugin의 판
- 독자가 더 쉽다고 고른 판은 구조를 바꾼 판이었습니다. 문장 규칙만 적용한 판은 지시만 받은 판에 15쌍 중 14쌍에서 졌습니다.
- 지시만 받은 판은 사람이 쓴 글까지 고쳐 쓰고, 원문에 없는 인과를 넣었습니다. 이 plugin은 그 고쳐 쓰기를 본체로 삼고 사실 보호 장치를 더했습니다. 지시만 받은 판과의 비교는 12쌍에서 5승 6패 1무였고, 새 주장은 0건이었습니다.

## License

MIT. 절차의 일부는 [declauding](https://github.com/oaustegard/claude-skills)(Oskar Austegard, MIT)에서 왔습니다.
