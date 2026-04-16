"""
TITLE: 모음 세기
DIFFICULTY: medium
TAGS: for, if, string, lower

DESCRIPTION:
문자열을 입력받아 대소문자 구분 없이 모음(a, e, i, o, u)의 개수를 세어
`모음 개수: N` 형태로 출력하시오.

예시:
- 입력: `Hello World` → 출력: `모음 개수: 3`
"""
# META_TESTS:
# - stdin: "Hello World"
#   expected_stdout: "모음 개수: 3"
# - stdin: "Python"
#   expected_stdout: "모음 개수: 1"
# - stdin: "AEIOU"
#   expected_stdout: "모음 개수: 5"

# lower()로 소문자 변환 후 비교
text = input()
vowel_count = 0
# TODO
print("모음 개수:", vowel_count)
