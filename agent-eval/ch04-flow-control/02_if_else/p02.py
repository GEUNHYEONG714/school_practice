"""
TITLE: 가위바위보 (컴퓨터는 바위 고정)
DIFFICULTY: easy
TAGS: if, elif, else, string, comparison

EVAL: stdio

DESCRIPTION:
컴퓨터는 항상 `바위`를 냅니다. 사용자가 낸 값을 입력받아 아래 형식으로 3줄을 출력하시오.

```
컴퓨터: 바위
나: {사용자}
결과: {결과}
```

결과 기준:
- 사용자가 `바위`면 `비겼습니다`
- 사용자가 `가위`면 `졌습니다`
- 사용자가 `보`면 `이겼습니다`
- 그 외 입력은 `잘못된 입력입니다`

예시:
- 입력: `가위` → 출력: `컴퓨터: 바위\n나: 가위\n결과: 졌습니다`
- 입력: `보` → 출력: `컴퓨터: 바위\n나: 보\n결과: 이겼습니다`
"""
# META_TESTS:
# - stdin: "가위"
#   expected_stdout: "컴퓨터: 바위\n나: 가위\n결과: 졌습니다"
# - stdin: "보"
#   expected_stdout: "컴퓨터: 바위\n나: 보\n결과: 이겼습니다"
# - stdin: "바위"
#   expected_stdout: "컴퓨터: 바위\n나: 바위\n결과: 비겼습니다"

# 컴퓨터는 "바위" 고정. 사용자 입력과 비교하여 결과를 출력하세요.
computer = "바위"
user = input()
# TODO
