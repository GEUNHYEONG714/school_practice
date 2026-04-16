"""
TITLE: 평균 구하기 (0 종료)
DIFFICULTY: easy
TAGS: while, sentinel, average

EVAL: stdio

DESCRIPTION:
숫자를 반복해서 입력받고, `0`이 입력되면 종료합니다.
입력한 숫자(0 제외)들의 평균을 `평균: 값` 형식(f-string, float 결과)으로 출력하시오.
단, 입력한 숫자가 하나도 없으면 `입력한 숫자가 없습니다.`를 출력하시오.

예시:
- 입력: `10\n20\n30\n0` → 출력: `평균: 20.0`
- 입력: `0` → 출력: `입력한 숫자가 없습니다.`
"""
# META_TESTS:
# - stdin: "10\n20\n30\n0"
#   expected_stdout: "평균: 20.0"
# - stdin: "0"
#   expected_stdout: "입력한 숫자가 없습니다."
# - stdin: "5\n15\n0"
#   expected_stdout: "평균: 10.0"

# 첫 입력을 먼저 받고 while num != 0 으로 반복하며 다음 입력을 받으세요.
total = 0
count = 0
# TODO
