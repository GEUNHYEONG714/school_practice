"""
TITLE: 약수 구하기
DIFFICULTY: easy
TAGS: for, range, divisor, modulo

EVAL: stdio

DESCRIPTION:
숫자 N을 입력받아 그 수의 약수를 모두 한 줄에 공백으로 구분하여 출력하시오.
출력 형식: `N의 약수: d1 d2 d3 ...` (각 숫자 뒤에 공백, 마지막에 줄바꿈)

예시:
- 입력: `12` → 출력: `12의 약수: 1 2 3 4 6 12 `
- 입력: `7` → 출력: `7의 약수: 1 7 `
"""
# META_TESTS:
# - stdin: "12"
#   expected_stdout: "12의 약수: 1 2 3 4 6 12 "
# - stdin: "7"
#   expected_stdout: "7의 약수: 1 7 "
# - stdin: "1"
#   expected_stdout: "1의 약수: 1 "

# "N의 약수: "를 end=" "로 출력한 뒤, 1부터 N까지 나머지가 0인 수를 end=" "로 출력하세요.
n = int(input())
# TODO
