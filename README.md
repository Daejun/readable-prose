# prose

A Claude Code plugin that makes model-written prose easier to read on the first pass. Rules are in Korean; they apply to Korean answers and to English commit messages, PR bodies and review replies.

Claude Code가 쓴 글을 처음 읽을 때 이해되게 만드는 plugin입니다.

## 설치

```
/plugin marketplace add Daejun/readable-prose
/plugin install prose@readable-prose
```

GitHub SSH key가 없는 machine에서는 `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1`을 설정한 뒤 실행합니다.

## 들어 있는 것

| 구성 | 하는 일 | context 비용 |
|---|---|---|
| `SessionStart` hook | session 시작, `/clear`, compaction 때 쓰기 규칙 5줄(`hooks/writing-rules.md`)을 context에 넣습니다 | session마다 약 1,000자 |
| `readable` skill | 글을 고쳐 쓸 때 구조를 바꾸고(결론 먼저, label 붙은 목록, 한 문장에 판정 하나) 원문과 대조해 사실을 지킵니다 | skill을 부를 때 약 3,300자 |
| `PreToolUse` hook | GitHub에 글을 올리는 `gh` 명령을, 그 turn에 skill을 부르기 전까지 막습니다 | 막을 때만 한 줄 |

skill은 "읽기 쉽게", "AI 문체", "다듬어", "make this readable" 같은 요청에 불립니다. 직접 부르려면 `/prose:readable`을 씁니다.

작업 도중에 게시할 때는 skill이 잘 불리지 않습니다. 그래서 `PreToolUse` hook이 아래 명령을 막고 skill을 먼저 부르라고 알립니다. 한 turn에서 skill을 한 번 부르면 그 turn의 나머지 명령은 막지 않습니다.

- `gh pr create`, `gh issue create`, `gh pr comment`, `gh issue comment`
- `--body`가 붙은 `gh pr review`, `gh pr edit`, `gh issue edit`
- field나 `--input`을 보내는 `gh api .../comments`, `gh api .../reviews`

이 hook을 끄려면 `READABLE_PROSE_GATE=0`을 설정합니다. hook은 `python3`를 쓰고, `python3`가 없거나 오류가 나면 명령을 막지 않습니다.

## skill이 불리는지 확인한 결과

`claude plugin eval`(`evals/`)과 실제 설정에서 띄운 `claude -p`로 쟀습니다.

- 글을 써 달라는 요청(PR 본문, commit message, review 답글, 보고서, 고쳐 쓰기): 모두 불렸습니다.
- 관계없는 질문(code 질문, 계산, 개념 설명): 한 번도 불리지 않았습니다.
- 코드를 고친 뒤 "commit해 주세요": skill은 3번 중 1번만 불렸습니다. skill을 강제로 부르면 commit turn이 몇 초씩 길어졌습니다. 그런데 skill로 달라진 것은 형식(72열, 문단 나누기, 목록)뿐이었습니다. 그래서 commit은 막지 않고, 형식을 쓰기 규칙 한 줄로 옮겼습니다. 규칙만으로 commit message 10개가 모두 72열 안에 들고 문제와 해결 문단이 나뉘었습니다.

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
