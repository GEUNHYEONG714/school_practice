"""
TITLE: 별 사각형
DIFFICULTY: easy
TAGS: for, nested-loop, print, string-multiply
EVAL: stdio

DESCRIPTION:
가로와 세로를 입력받아 해당 크기의 별(*) 사각형을 출력하시오.

예시:
- 입력: `5\n3` → 가로 5, 세로 3인 별 사각형
  ```
  *****
  *****
  *****
  ```
"""
# META_TESTS:
# - stdin: "5\n3"
#   expected_stdout: "*****\n*****\n*****"
# - stdin: "3\n2"
#   expected_stdout: "***\n***"
# - stdin: "1\n4"
#   expected_stdout: "*\n*\n*\n*"

# 가로와 세로를 입력받아 별(*) 사각형을 출력하세요.
width = int(input())
height = int(input())
# TODO
