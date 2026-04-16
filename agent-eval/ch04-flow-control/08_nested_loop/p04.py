"""
TITLE: 역삼각형 별 찍기
DIFFICULTY: medium
TAGS: nested-loop, for, pattern, stars

DESCRIPTION:
줄 수 N을 입력받아, 첫 줄은 별 N개, 마지막 줄은 별 1개가 되도록
역삼각형을 출력하시오.

예시:
- 입력: `3` → 출력: `***\n**\n*`
- 입력: `5` → 출력: `*****\n****\n***\n**\n*`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "***\n**\n*"
# - stdin: "5"
#   expected_stdout: "*****\n****\n***\n**\n*"
# - stdin: "1"
#   expected_stdout: "*"

# range(n, 0, -1)은 n부터 1까지 감소합니다.
n = int(input())
# TODO
