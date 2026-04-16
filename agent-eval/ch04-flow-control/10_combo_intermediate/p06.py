"""
TITLE: 최대공약수 (유클리드 호제법)
DIFFICULTY: hard
TAGS: algorithm, math, gcd, while
EVAL: stdio

DESCRIPTION:
두 정수 a, b를 각 줄에 입력받아 유클리드 호제법으로 최대공약수를 구합니다.
첫 줄: `GCD(a, b) 계산 과정:`
이후 각 단계: `  a ÷ b = q ... 나머지 r`
마지막 줄: `최대공약수: g`

예시:
- 입력: `48\n18` → 출력:
```
GCD(48, 18) 계산 과정:
  48 ÷ 18 = 2 ... 나머지 12
  18 ÷ 12 = 1 ... 나머지 6
  12 ÷ 6 = 2 ... 나머지 0
최대공약수: 6
```
"""
# META_TESTS:
# - stdin: "48\n18"
#   expected_stdout: "GCD(48, 18) 계산 과정:\n  48 ÷ 18 = 2 ... 나머지 12\n  18 ÷ 12 = 1 ... 나머지 6\n  12 ÷ 6 = 2 ... 나머지 0\n최대공약수: 6"
# - stdin: "12\n8"
#   expected_stdout: "GCD(12, 8) 계산 과정:\n  12 ÷ 8 = 1 ... 나머지 4\n  8 ÷ 4 = 2 ... 나머지 0\n최대공약수: 4"
# - stdin: "7\n5"
#   expected_stdout: "GCD(7, 5) 계산 과정:\n  7 ÷ 5 = 1 ... 나머지 2\n  5 ÷ 2 = 2 ... 나머지 1\n  2 ÷ 1 = 2 ... 나머지 0\n최대공약수: 1"

# 유클리드 호제법으로 GCD를 구하세요.
a = int(input())
b = int(input())
# TODO
