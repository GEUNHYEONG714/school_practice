"""
TITLE: 진법 변환 (10진법 → 8진법)
DIFFICULTY: medium
TAGS: while, if, arithmetic, modulo
EVAL: stdio

DESCRIPTION:
10진법 정수를 입력받아 8진법으로 변환하여 출력하시오.

출력 형식: 변환된 8진법 숫자를 그대로 출력합니다.
(내장 함수 oct() 사용 금지, 반복문으로 직접 변환)

예시:
- 입력: `10` → 출력: `12`
- 입력: `8` → 출력: `10`
"""
# META_TESTS:
# - stdin: "10"
#   expected_stdout: "12"
# - stdin: "8"
#   expected_stdout: "10"
# - stdin: "100"
#   expected_stdout: "144"

# 10진법 정수를 8진법으로 변환하여 출력하세요. (oct() 사용 금지)
n = int(input())
# TODO
