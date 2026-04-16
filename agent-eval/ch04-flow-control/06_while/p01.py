"""
TITLE: 카운트다운
DIFFICULTY: easy
TAGS: while, decrement

EVAL: stdio

DESCRIPTION:
시작 숫자 N을 입력받아 N부터 1까지 줄바꿈하며 출력한 뒤, 마지막에 `발사!`를 출력하시오.

예시:
- 입력: `5` → 출력:
  ```
  5
  4
  3
  2
  1
  발사!
  ```
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "5\n4\n3\n2\n1\n발사!"
# - stdin: "1"
#   expected_stdout: "1\n발사!"
# - stdin: "3"
#   expected_stdout: "3\n2\n1\n발사!"

# while n >= 1: print(n); n -= 1 후 "발사!" 출력.
n = int(input())
# TODO
