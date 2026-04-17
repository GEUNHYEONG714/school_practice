"""
TITLE: 단어 첫 글자 대문자 변환
DIFFICULTY: medium
TAGS: for, if, string, flag
EVAL: stdio

DESCRIPTION:
문장을 입력받아 각 단어의 첫 글자만 대문자로 변환하여 출력하시오.

split()을 사용하지 않고, for문으로 문자열을 한 글자씩 순회합니다.
공백 바로 다음에 오는 글자와 문장의 첫 글자를 대문자로 변환합니다.

예시:
- 입력: `hello world` → 출력: `Hello World`
- 입력: `python is fun` → 출력: `Python Is Fun`
"""
# META_TESTS:
# - stdin: "hello world"
#   expected_stdout: "Hello World"
# - stdin: "python is fun"
#   expected_stdout: "Python Is Fun"
# - stdin: "abc"
#   expected_stdout: "Abc"

# for문과 플래그 변수를 사용하세요. upper() 메서드를 활용하세요.
s = input()
result = ""
# TODO
