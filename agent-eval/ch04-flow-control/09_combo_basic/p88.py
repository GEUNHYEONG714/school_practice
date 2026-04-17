"""
TITLE: 구간 소수
DIFFICULTY: medium
TAGS: for, while, if, nested-loop, modulo, break
EVAL: stdio

DESCRIPTION:
시작과 끝 정수를 입력받아 해당 구간의 소수만 출력하시오.

출력 형식: 소수를 한 줄에 공백으로 구분하여 출력합니다.

예시:
- 입력: `10\n20` → 출력: `11 13 17 19`
"""
# META_TESTS:
# - stdin: "10\n20"
#   expected_stdout: "11 13 17 19"
# - stdin: "1\n10"
#   expected_stdout: "2 3 5 7"
# - stdin: "20\n30"
#   expected_stdout: "23 29"

# 구간 내 소수를 찾아 출력하세요.
start = int(input())
end = int(input())
# TODO
