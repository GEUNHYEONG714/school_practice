"""
TITLE: 자릿수 합 구하기
DIFFICULTY: medium
TAGS: while, modulo, digit
EVAL: stdio

DESCRIPTION:
자연수를 입력받아 각 자릿수의 합을 `각 자릿수의 합: 값` 형식으로 출력하시오.

예시:
- 입력: `1234` → 출력: `각 자릿수의 합: 10`
- 입력: `567` → 출력: `각 자릿수의 합: 18`
"""
# META_TESTS:
# - stdin: "1234"
#   expected_stdout: "각 자릿수의 합: 10"
# - stdin: "567"
#   expected_stdout: "각 자릿수의 합: 18"
# - stdin: "9"
#   expected_stdout: "각 자릿수의 합: 9"

# while문과 %10, //10을 사용하세요.
num = int(input())
# TODO
