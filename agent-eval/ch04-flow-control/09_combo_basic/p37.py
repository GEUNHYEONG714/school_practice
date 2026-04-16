"""
TITLE: 특정 문자 제거
DIFFICULTY: medium
TAGS: for, if, string

DESCRIPTION:
첫 줄에 문자열, 둘째 줄에 제거할 문자를 입력받아
해당 문자를 제외한 나머지를 `결과: ...` 형태로 출력하시오.
`replace()`는 사용하지 말 것.

예시:
- 입력: `hello world`, `l` → 출력: `결과: heo word`
"""
# META_TESTS:
# - stdin: "hello world\nl"
#   expected_stdout: "결과: heo word"
# - stdin: "banana\na"
#   expected_stdout: "결과: bnn"
# - stdin: "abc\nx"
#   expected_stdout: "결과: abc"

# for + if char != remove: result += char
text = input()
remove = input()
result = ""
# TODO
print("결과:", result)
