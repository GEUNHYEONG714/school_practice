"""
TITLE: 팩토리얼 합
DIFFICULTY: hard
TAGS: algorithm, math, factorial, loop
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 각 팩토리얼 값을 `i! = v` 형식으로 한 줄씩 출력하고,
마지막에 `1! + 2! + ... + N! = 합` 형식으로 총합을 출력합니다.

예시:
- 입력: `5` → 출력:
```
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
1! + 2! + 3! + 4! + 5! = 153
```
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "1! = 1\n2! = 2\n3! = 6\n4! = 24\n5! = 120\n1! + 2! + 3! + 4! + 5! = 153"
# - stdin: "3"
#   expected_stdout: "1! = 1\n2! = 2\n3! = 6\n1! + 2! + 3! = 9"
# - stdin: "1"
#   expected_stdout: "1! = 1\n1! = 1"

# 1!부터 N!까지 출력하고 합을 구하세요.
n = int(input())
# TODO
