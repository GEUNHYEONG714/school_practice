"""
TITLE: 완전수 찾기
DIFFICULTY: hard
TAGS: algorithm, math, divisor, loop
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 2부터 N 사이의 모든 완전수를 `N = d1 + d2 + ...` 형식으로 출력합니다.
완전수란 자기 자신을 제외한 약수의 합이 자기 자신과 같은 수입니다.

예시:
- 입력: `30` → 출력:
```
6 = 1 + 2 + 3
28 = 1 + 2 + 4 + 7 + 14
```
"""
# META_TESTS:
# - stdin: "30"
#   expected_stdout: "6 = 1 + 2 + 3\n28 = 1 + 2 + 4 + 7 + 14"
# - stdin: "10"
#   expected_stdout: "6 = 1 + 2 + 3"
# - stdin: "500"
#   expected_stdout: "6 = 1 + 2 + 3\n28 = 1 + 2 + 4 + 7 + 14\n496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248"

# 2부터 N까지 완전수를 찾아 출력하세요.
n = int(input())
# TODO
