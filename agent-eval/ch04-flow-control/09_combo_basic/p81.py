"""
TITLE: 단어 뒤집기 (문장)
DIFFICULTY: medium
TAGS: for, if, string
EVAL: stdio

DESCRIPTION:
문장을 입력받아 각 단어를 뒤집어서 출력하시오. 공백 위치는 유지합니다.

split()을 사용하지 않고 for문으로 문자열을 순회합니다.
공백을 만나면 지금까지 모은 단어를 뒤집어 결과에 추가하고,
문자열 끝에서도 마지막 단어를 뒤집어 추가합니다.

예시:
- 입력: `hello world` → 출력: `olleh dlrow`
- 입력: `python is fun` → 출력: `nohtyp si nuf`
"""
# META_TESTS:
# - stdin: "hello world"
#   expected_stdout: "olleh dlrow"
# - stdin: "python is fun"
#   expected_stdout: "nohtyp si nuf"
# - stdin: "abc"
#   expected_stdout: "cba"

# for문으로 순회하며 단어를 모으고 공백을 만나면 뒤집으세요.
s = input()
result = ""
word = ""
# TODO
