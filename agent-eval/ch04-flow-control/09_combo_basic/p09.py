"""
TITLE: 간단한 계산기
DIFFICULTY: medium
TAGS: if, elif, else, nested
EVAL: stdio

DESCRIPTION:
첫 번째 수(실수), 연산자(문자열), 두 번째 수(실수)를 각각 한 줄씩 입력받아 계산 결과를 출력하시오.

- `+`, `-`, `*`, `/` 연산자를 지원합니다.
- 각 연산자에 대해 `num1 + num2 = result` 같은 형식으로 출력 (print 사이에 공백 자동 삽입).
  예: `print(num1, "+", num2, "=", result)` → `10.0 + 3.0 = 13.0`
- `/`에서 num2 == 0이면 `0으로 나눌 수 없습니다.` 출력.
- 지원하지 않는 연산자면 `지원하지 않는 연산자입니다.` 출력.

예시:
- 입력: `10\n+\n3` → 출력: `10.0 + 3.0 = 13.0`
- 입력: `10\n/\n0` → 출력: `0으로 나눌 수 없습니다.`
- 입력: `5\n%\n2` → 출력: `지원하지 않는 연산자입니다.`
"""
# META_TESTS:
# - stdin: "10\n+\n3"
#   expected_stdout: "10.0 + 3.0 = 13.0"
# - stdin: "10\n/\n0"
#   expected_stdout: "0으로 나눌 수 없습니다."
# - stdin: "5\n%\n2"
#   expected_stdout: "지원하지 않는 연산자입니다."

# 연산자를 if/elif로 판별하고 나누기에서 0 체크를 추가하세요.
num1 = float(input())
op = input()
num2 = float(input())
# TODO
