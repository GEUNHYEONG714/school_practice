"""
TITLE: 문자열 한 글자씩 출력
DIFFICULTY: easy
TAGS: for, string, iteration

EVAL: stdio

DESCRIPTION:
이름(문자열)을 입력받아 한 글자씩 줄바꿈하여 출력하시오.

예시:
- 입력: `홍길동` → 출력:
  ```
  홍
  길
  동
  ```
"""
# META_TESTS:
# - stdin: "홍길동"
#   expected_stdout: "홍\n길\n동"
# - stdin: "abc"
#   expected_stdout: "a\nb\nc"
# - stdin: "K"
#   expected_stdout: "K"

# for ch in name: print(ch) 형태로 작성하세요.
name = input()
# TODO
