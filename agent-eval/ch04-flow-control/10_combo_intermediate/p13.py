"""
TITLE: 두 수의 합 (Two Sum)
DIFFICULTY: hard
TAGS: algorithm, math, loop
EVAL: stdio

DESCRIPTION:
정수 N과 target을 각 줄에 입력받아, 1부터 N까지 수 중 합이 target이 되는 서로 다른 두 수 쌍 (a < b)을
`(a, b)` 형식으로 모두 출력합니다.

예시:
- 입력: `10\n10` → 출력:
```
(1, 9)
(2, 8)
(3, 7)
(4, 6)
```
"""
# META_TESTS:
# - stdin: "10\n10"
#   expected_stdout: "(1, 9)\n(2, 8)\n(3, 7)\n(4, 6)"
# - stdin: "5\n6"
#   expected_stdout: "(1, 5)\n(2, 4)"
# - stdin: "6\n7"
#   expected_stdout: "(1, 6)\n(2, 5)\n(3, 4)"

# 합이 target인 두 수의 쌍을 출력하세요.
N = int(input())
target = int(input())
# TODO
