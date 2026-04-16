"""
TITLE: 문자열 뒤집기
DIFFICULTY: medium
TAGS: for, range, string, index

DESCRIPTION:
문자열을 입력받아 슬라이싱을 사용하지 않고 for + range로 거꾸로 뒤집어
`뒤집은 문자열: ...` 형태로 출력하시오.

예시:
- 입력: `python` → 출력: `뒤집은 문자열: nohtyp`
"""
# META_TESTS:
# - stdin: "python"
#   expected_stdout: "뒤집은 문자열: nohtyp"
# - stdin: "hello"
#   expected_stdout: "뒤집은 문자열: olleh"
# - stdin: "a"
#   expected_stdout: "뒤집은 문자열: a"

# range(len(text)-1, -1, -1)로 역순 순회
text = input()
result = ""
# TODO
print("뒤집은 문자열:", result)
