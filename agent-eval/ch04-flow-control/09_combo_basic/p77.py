"""
TITLE: 두 문자열 교차 출력
DIFFICULTY: medium
TAGS: for, if, string, index
EVAL: stdio

DESCRIPTION:
두 문자열을 한 줄씩 입력받아 한 글자씩 교차로 합쳐 출력하시오.
길이가 다르면 긴 쪽의 나머지 글자를 뒤에 이어붙입니다.

예시:
- 입력: `ab\n12` → 출력: `a1b2`
- 입력: `abcd\n12` → 출력: `a1b2cd`
"""
# META_TESTS:
# - stdin: "ab\n12"
#   expected_stdout: "a1b2"
# - stdin: "abcd\n12"
#   expected_stdout: "a1b2cd"
# - stdin: "x\nABC"
#   expected_stdout: "xABC"

# while 또는 for + range를 사용하여 인덱스로 접근하세요.
s1 = input()
s2 = input()
result = ""
# TODO
