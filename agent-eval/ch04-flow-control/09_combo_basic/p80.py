"""
TITLE: 괄호 짝 검사
DIFFICULTY: easy
TAGS: for, if, string, counter
EVAL: stdio

DESCRIPTION:
문자열을 입력받아 여는 괄호 "("와 닫는 괄호 ")"의 개수가 같으면 "올바름",
다르면 "올바르지 않음"을 출력하시오.

for문으로 문자열을 순회하며 괄호 개수를 세세요.

예시:
- 입력: `(a+b)*(c+d)` → 여는 2개, 닫는 2개 → 출력: `올바름`
- 입력: `((a+b)` → 여는 2개, 닫는 1개 → 출력: `올바르지 않음`
"""
# META_TESTS:
# - stdin: "(a+b)*(c+d)"
#   expected_stdout: "올바름"
# - stdin: "((a+b)"
#   expected_stdout: "올바르지 않음"
# - stdin: "hello"
#   expected_stdout: "올바름"

# for문으로 순회하며 '('와 ')'의 개수를 각각 세세요.
s = input()
# TODO
