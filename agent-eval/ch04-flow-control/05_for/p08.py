"""
TITLE: 팩토리얼 계산
DIFFICULTY: easy
TAGS: for, range, accumulator, factorial

EVAL: stdio

DESCRIPTION:
숫자 N을 입력받아 N!(팩토리얼)을 `N! = 값` 형식으로 출력하시오.
N!은 1부터 N까지의 모든 수의 곱입니다.
(print(str(n) + "! =", result) 사용 — `!` 와 `=` 사이에 공백 하나)

예시:
- 입력: `5` → 출력: `5! = 120`
- 입력: `1` → 출력: `1! = 1`
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "5! = 120"
# - stdin: "1"
#   expected_stdout: "1! = 1"
# - stdin: "10"
#   expected_stdout: "10! = 3628800"

# 누적 곱 변수의 초깃값은 1로 두세요.
n = int(input())
# TODO
