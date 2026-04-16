"""
TITLE: 문자열 길이 세기
DIFFICULTY: medium
TAGS: for, string, count

DESCRIPTION:
문자열을 입력받아 `len()` 함수를 사용하지 않고 for문으로 한 글자씩 세어
`문자열 길이: N` 형태로 출력하시오.

예시:
- 입력: `hello` → 출력: `문자열 길이: 5`
"""
# META_TESTS:
# - stdin: "hello"
#   expected_stdout: "문자열 길이: 5"
# - stdin: "python"
#   expected_stdout: "문자열 길이: 6"
# - stdin: "a"
#   expected_stdout: "문자열 길이: 1"

# for char in text: 로 한 글자씩 순회
text = input()
count = 0
# TODO
print("문자열 길이:", count)
