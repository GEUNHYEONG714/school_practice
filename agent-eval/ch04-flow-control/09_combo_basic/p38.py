"""
TITLE: 단어 마스킹
DIFFICULTY: medium
TAGS: for, range, if, index

DESCRIPTION:
문자열을 입력받아 첫 글자와 마지막 글자만 그대로 두고 나머지는 `*`로 바꿔
`마스킹 결과: ...` 형태로 출력하시오.

예시:
- 입력: `python` → 출력: `마스킹 결과: p****n`
"""
# META_TESTS:
# - stdin: "python"
#   expected_stdout: "마스킹 결과: p****n"
# - stdin: "hi"
#   expected_stdout: "마스킹 결과: hi"
# - stdin: "abc"
#   expected_stdout: "마스킹 결과: a*c"

# 인덱스 0과 len-1만 원래 글자, 나머지는 *
text = input()
result = ""
# TODO
print("마스킹 결과:", result)
