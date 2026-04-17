"""
TITLE: 모음 제거
DIFFICULTY: easy
TAGS: for, if, string
EVAL: stdio

DESCRIPTION:
문장을 입력받아 영어 모음(a, e, i, o, u, A, E, I, O, U)을 모두 제거한 결과를 출력하시오.

for문으로 문자열을 순회하며 모음이 아닌 문자만 결과에 추가합니다.

예시:
- 입력: `Hello World` → 출력: `Hll Wrld`
- 입력: `Python` → 출력: `Pythn`
"""
# META_TESTS:
# - stdin: "Hello World"
#   expected_stdout: "Hll Wrld"
# - stdin: "Python"
#   expected_stdout: "Pythn"
# - stdin: "AEIOUaeiou"
#   expected_stdout: ""

# for문으로 순회하며 모음 여부를 확인하세요.
s = input()
result = ""
# TODO
