"""
TITLE: 음수 입력시 종료
DIFFICULTY: medium
TAGS: while, break, sentinel

EVAL: stdio

DESCRIPTION:
숫자를 계속 입력받다가 음수가 입력되면 종료합니다.
종료 후 지금까지 입력받은 양수(및 0)의 합을 `합계: 값` 형식으로 출력하시오.
(출력은 `print("합계:", total)` — 콤마로 공백 하나 포함)

예시:
- 입력: `10\n20\n5\n-1` → 출력: `합계: 35`
- 입력: `-5` → 출력: `합계: 0`
"""
# META_TESTS:
# - stdin: "10\n20\n5\n-1"
#   expected_stdout: "합계: 35"
# - stdin: "-5"
#   expected_stdout: "합계: 0"
# - stdin: "0\n7\n3\n-2"
#   expected_stdout: "합계: 10"

# while True 안에서 음수면 break, 아니면 total에 누적.
total = 0
# TODO
