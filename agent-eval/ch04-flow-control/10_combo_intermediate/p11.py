"""
TITLE: 쌍둥이 소수
DIFFICULTY: hard
TAGS: algorithm, math, prime, loop
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 1부터 N 사이의 쌍둥이 소수 쌍(차이가 2인 두 소수)을 `(a, b)` 형식으로 출력합니다.
두 소수 모두 N 이하여야 합니다.

예시:
- 입력: `50` → 출력:
```
(3, 5)
(5, 7)
(11, 13)
(17, 19)
(29, 31)
(41, 43)
```
"""
# META_TESTS:
# - stdin: "50"
#   expected_stdout: "(3, 5)\n(5, 7)\n(11, 13)\n(17, 19)\n(29, 31)\n(41, 43)"
# - stdin: "20"
#   expected_stdout: "(3, 5)\n(5, 7)\n(11, 13)\n(17, 19)"
# - stdin: "10"
#   expected_stdout: "(3, 5)\n(5, 7)"

# 1부터 N 사이의 쌍둥이 소수 쌍을 출력하세요.
N = int(input())
# TODO
