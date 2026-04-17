"""
TITLE: 카멜케이스 변환
DIFFICULTY: medium
TAGS: for, if, string, flag
EVAL: stdio

DESCRIPTION:
언더스코어(_)로 연결된 문자열을 입력받아 카멜케이스로 변환하여 출력하시오.

카멜케이스 규칙:
- 첫 단어는 소문자로 시작
- 이후 단어의 첫 글자만 대문자로 변환
- 언더스코어는 제거

for문으로 문자열을 순회하며 변환합니다. split() 사용 금지.

예시:
- 입력: `hello_world` → 출력: `helloWorld`
- 입력: `my_variable_name` → 출력: `myVariableName`
"""
# META_TESTS:
# - stdin: "hello_world"
#   expected_stdout: "helloWorld"
# - stdin: "my_variable_name"
#   expected_stdout: "myVariableName"
# - stdin: "single"
#   expected_stdout: "single"

# for문으로 순회하며 '_' 다음 문자를 대문자로 변환하세요.
s = input()
result = ""
# TODO
