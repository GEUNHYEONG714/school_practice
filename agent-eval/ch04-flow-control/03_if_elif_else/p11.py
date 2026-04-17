"""
TITLE: 비밀번호 강도 판별
DIFFICULTY: easy
TAGS: if, elif, else, len, string
EVAL: stdio

DESCRIPTION:
비밀번호를 입력받아 길이에 따라 강도를 출력하시오.
- 8자 이상: `강함`
- 4자 이상: `보통`
- 그 외: `약함`

힌트: len() 함수로 문자열 길이를 구할 수 있습니다.

예시:
- 입력: `python12` → 출력: `강함`
- 입력: `abcd` → 출력: `보통`
- 입력: `hi` → 출력: `약함`
"""
# META_TESTS:
# - stdin: "python12"
#   expected_stdout: "강함"
# - stdin: "abcd"
#   expected_stdout: "보통"
# - stdin: "hi"
#   expected_stdout: "약함"
# - stdin: "abcdefgh"
#   expected_stdout: "강함"
# - stdin: "abc"
#   expected_stdout: "약함"

# 비밀번호를 입력받아 길이에 따라 강도를 출력하세요.
password = input()
# TODO
