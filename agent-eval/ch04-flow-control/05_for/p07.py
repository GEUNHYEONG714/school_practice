"""
TITLE: 거꾸로 카운트
DIFFICULTY: easy
TAGS: for, range, step

EVAL: stdio

DESCRIPTION:
숫자 N을 입력받아 N부터 1까지 한 줄에 하나씩 거꾸로 출력하시오.
range의 step 인자에 -1을 사용합니다.

예시:
- 입력: `5` → 출력:
  ```
  5
  4
  3
  2
  1
  ```
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "5\n4\n3\n2\n1"
# - stdin: "1"
#   expected_stdout: "1"
# - stdin: "3"
#   expected_stdout: "3\n2\n1"

# range(n, 0, -1)을 사용하세요.
n = int(input())
# TODO
