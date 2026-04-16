"""
TITLE: 입장 판정
DIFFICULTY: easy
TAGS: nested, if, else, string

EVAL: stdio

DESCRIPTION:
나이와 티켓 보유 여부(`Y`/`N`)를 순서대로 입력받아 입장 가능 여부를 출력하시오.

- 18세 이상:
  - 티켓이 `Y`이면 `입장 가능합니다.`
  - 티켓이 `N`이면 `티켓을 구매해주세요.`
- 18세 미만: `18세 미만은 입장할 수 없습니다.`

예시:
- 입력: `20\nY` → 출력: `입장 가능합니다.`
- 입력: `20\nN` → 출력: `티켓을 구매해주세요.`
- 입력: `15\nY` → 출력: `18세 미만은 입장할 수 없습니다.`
"""
# META_TESTS:
# - stdin: "20\nY"
#   expected_stdout: "입장 가능합니다."
# - stdin: "20\nN"
#   expected_stdout: "티켓을 구매해주세요."
# - stdin: "15\nY"
#   expected_stdout: "18세 미만은 입장할 수 없습니다."

# 나이와 티켓 두 값을 먼저 입력받고, 중첩 if문으로 판정하세요.
age = int(input())
ticket = input()
# TODO
