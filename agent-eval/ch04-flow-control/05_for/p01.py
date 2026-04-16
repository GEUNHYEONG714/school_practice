"""
TITLE: 구구단 출력
DIFFICULTY: easy
TAGS: for, range, multiplication

EVAL: stdio

DESCRIPTION:
단 수를 입력받아 해당 구구단을 1단부터 9단까지 출력하시오.
출력 형식은 `N x i = 값` 입니다.

예시:
- 입력: `3` → 출력:
  ```
  3 x 1 = 3
  3 x 2 = 6
  ...
  3 x 9 = 27
  ```
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27"
# - stdin: "1"
#   expected_stdout: "1 x 1 = 1\n1 x 2 = 2\n1 x 3 = 3\n1 x 4 = 4\n1 x 5 = 5\n1 x 6 = 6\n1 x 7 = 7\n1 x 8 = 8\n1 x 9 = 9"
# - stdin: "9"
#   expected_stdout: "9 x 1 = 9\n9 x 2 = 18\n9 x 3 = 27\n9 x 4 = 36\n9 x 5 = 45\n9 x 6 = 54\n9 x 7 = 63\n9 x 8 = 72\n9 x 9 = 81"

# for + range(1, 10)을 사용해 구구단 한 단을 출력하세요.
dan = int(input())
# TODO
