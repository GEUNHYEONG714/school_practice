"""
TITLE: 홀수만 출력
DIFFICULTY: easy
TAGS: for, range, modulo, if

EVAL: stdio

DESCRIPTION:
숫자 N을 입력받아 1부터 N까지의 수 중 홀수만 한 줄에 하나씩 출력하시오.

예시:
- 입력: `10` → 출력:
  ```
  1
  3
  5
  7
  9
  ```
"""
# META_TESTS:
# - stdin: "10"
#   expected_stdout: "1\n3\n5\n7\n9"
# - stdin: "1"
#   expected_stdout: "1"
# - stdin: "5"
#   expected_stdout: "1\n3\n5"

# 1부터 N까지 반복하며 i % 2 == 1인 경우에만 print(i)로 출력하세요.
n = int(input())
# TODO
