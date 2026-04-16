"""
TITLE: 최소공배수
DIFFICULTY: hard
TAGS: algorithm, math, gcd, lcm
EVAL: stdio

DESCRIPTION:
두 정수 a, b를 각 줄에 입력받아 최대공약수(GCD)와 최소공배수(LCM)를 출력합니다.
공식: LCM(a, b) = a × b ÷ GCD(a, b)

예시:
- 입력: `12\n18` → 출력:
```
최대공약수(GCD): 6
최소공배수(LCM): 36
```
"""
# META_TESTS:
# - stdin: "12\n18"
#   expected_stdout: "최대공약수(GCD): 6\n최소공배수(LCM): 36"
# - stdin: "4\n6"
#   expected_stdout: "최대공약수(GCD): 2\n최소공배수(LCM): 12"
# - stdin: "7\n3"
#   expected_stdout: "최대공약수(GCD): 1\n최소공배수(LCM): 21"

# 두 수의 GCD와 LCM을 출력하세요.
a = int(input())
b = int(input())
# TODO
