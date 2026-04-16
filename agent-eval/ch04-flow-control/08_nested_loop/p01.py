"""
TITLE: 별 찍기 삼각형
DIFFICULTY: medium
TAGS: nested-loop, for, pattern, stars

DESCRIPTION:
줄 수 N을 입력받아, 1번째 줄에 별 1개, 2번째 줄에 별 2개, ..., N번째 줄에 별 N개를
출력하는 삼각형을 출력하시오.

예시:
- 입력: `3` → 출력: `*\n**\n***`
- 입력: `5` → 출력: `*\n**\n***\n****\n*****`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "*\n**\n***"
# - stdin: "5"
#   expected_stdout: "*\n**\n***\n****\n*****"
# - stdin: "1"
#   expected_stdout: "*"

# 바깥 for문으로 줄, 안쪽 for문으로 별 개수를 제어하세요.
n = int(input())
# TODO
