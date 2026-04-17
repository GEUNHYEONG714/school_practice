"""
TITLE: 이진수 1의 개수
DIFFICULTY: easy
TAGS: while, if, arithmetic, modulo, counter
EVAL: stdio

DESCRIPTION:
정수를 입력받아 이진수로 변환했을 때 1의 개수를 출력하시오.

출력 형식: 숫자만 출력합니다.
(내장 함수 bin() 사용 금지, 반복문으로 직접 계산)

예시:
- 입력: `10` → 이진수 1010 → 출력: `2`
- 입력: `7` → 이진수 111 → 출력: `3`
"""
# META_TESTS:
# - stdin: "10"
#   expected_stdout: "2"
# - stdin: "7"
#   expected_stdout: "3"
# - stdin: "255"
#   expected_stdout: "8"

# 정수를 이진수로 변환하여 1의 개수를 출력하세요. (bin() 사용 금지)
n = int(input())
# TODO
