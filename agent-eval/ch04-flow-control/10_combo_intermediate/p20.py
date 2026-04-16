"""
TITLE: 연속된 수의 합으로 표현하기
DIFFICULTY: hard
TAGS: algorithm, math, loop
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 N을 2개 이상의 연속된 자연수의 합으로 표현하는 모든 경우를
`N = a + b + c + ...` 형식으로 출력합니다. (시작 수가 작은 것부터)

예시:
- 입력: `15` → 출력:
```
15 = 1 + 2 + 3 + 4 + 5
15 = 4 + 5 + 6
15 = 7 + 8
```
"""
# META_TESTS:
# - stdin: "15"
#   expected_stdout: "15 = 1 + 2 + 3 + 4 + 5\n15 = 4 + 5 + 6\n15 = 7 + 8"
# - stdin: "9"
#   expected_stdout: "9 = 2 + 3 + 4\n9 = 4 + 5"
# - stdin: "10"
#   expected_stdout: "10 = 1 + 2 + 3 + 4"

# N을 연속된 자연수의 합으로 표현하는 모든 경우를 출력하세요.
N = int(input())
# TODO
