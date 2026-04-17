"""
TITLE: 배수 판별기
DIFFICULTY: easy
TAGS: for, if, modulo, print
EVAL: stdio

DESCRIPTION:
숫자와 N을 입력받아 2부터 N까지 각각의 배수인지 판별하여 출력하시오.

출력 형식:
- 배수이면: `X의 배수입니다.`
- 배수가 아니면: `X의 배수가 아닙니다.`

예시:
- 입력: `12\n5` → 2~5의 배수 여부 각각 출력
"""
# META_TESTS:
# - stdin: "12\n5"
#   expected_stdout: "2의 배수입니다.\n3의 배수입니다.\n4의 배수입니다.\n5의 배수가 아닙니다."
# - stdin: "7\n3"
#   expected_stdout: "2의 배수가 아닙니다.\n3의 배수가 아닙니다."
# - stdin: "30\n6"
#   expected_stdout: "2의 배수입니다.\n3의 배수입니다.\n4의 배수가 아닙니다.\n5의 배수입니다.\n6의 배수입니다."

# 숫자와 N을 입력받아 2~N의 배수인지 각각 출력하세요.
num = int(input())
n = int(input())
# TODO
