"""
TITLE: 문자 종류 카운트
DIFFICULTY: medium
TAGS: for, if, elif, string, counter
EVAL: stdio

DESCRIPTION:
문자열을 입력받아 대문자, 소문자, 숫자, 기타 문자의 개수를 각각 출력하시오.

출력 형식 (4줄):
`대문자: X`
`소문자: X`
`숫자: X`
`기타: X`

예시:
- 입력: `Hello World! 123` → 대문자 2, 소문자 8, 숫자 3, 기타 3(공백2+!1)
"""
# META_TESTS:
# - stdin: "Hello World! 123"
#   expected_stdout: "대문자: 2\n소문자: 8\n숫자: 3\n기타: 3"
# - stdin: "ABC"
#   expected_stdout: "대문자: 3\n소문자: 0\n숫자: 0\n기타: 0"
# - stdin: "a1!b2@"
#   expected_stdout: "대문자: 0\n소문자: 2\n숫자: 2\n기타: 2"

# for문과 isupper(), islower(), isdigit()를 사용하세요.
s = input()
upper = 0
lower = 0
digit = 0
other = 0
# TODO
