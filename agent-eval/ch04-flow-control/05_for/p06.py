"""
TITLE: 별 한 줄 출력
DIFFICULTY: easy
TAGS: for, range, print-end

EVAL: stdio

DESCRIPTION:
숫자 N을 입력받아 별(`*`)을 N개 한 줄에 이어 출력하시오.
출력 후 줄바꿈을 해야 합니다.

예시:
- 입력: `5` → 출력: `*****`
- 입력: `1` → 출력: `*`
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "*****"
# - stdin: "1"
#   expected_stdout: "*"
# - stdin: "10"
#   expected_stdout: "**********"

# print("*", end="")으로 N번 출력한 뒤 print()로 줄바꿈하세요.
n = int(input())
# TODO
