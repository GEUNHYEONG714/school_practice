"""
TITLE: 친화수 찾기
DIFFICULTY: hard
TAGS: algorithm, math, divisor, loop
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 1부터 N 사이의 친화수 쌍을 `(a, b)` 형식으로 출력합니다. (a < b)
친화수: a의 진약수 합 = b, b의 진약수 합 = a 인 쌍 (a != b)

예시:
- 입력: `10000` → 출력:
```
(220, 284)
(1184, 1210)
(2620, 2924)
(5020, 5564)
(6232, 6368)
```
"""
# META_TESTS:
# - stdin: "10000"
#   expected_stdout: "(220, 284)\n(1184, 1210)\n(2620, 2924)\n(5020, 5564)\n(6232, 6368)"
# - stdin: "300"
#   expected_stdout: "(220, 284)"
# - stdin: "1500"
#   expected_stdout: "(220, 284)\n(1184, 1210)"

# 1부터 N 사이의 친화수 쌍을 출력하세요.
N = int(input())
# TODO
