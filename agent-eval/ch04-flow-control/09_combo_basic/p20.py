"""
TITLE: 누적합 100 초과 종료
DIFFICULTY: medium
TAGS: while, break, accumulator
EVAL: stdio

DESCRIPTION:
숫자를 반복 입력받아 누적합을 구하다가 누적합이 100을 넘는 순간 반복을 종료하시오.

종료 후 3줄을 출력:
`누적합이 100을 초과했습니다!`
`누적합: 값`
`입력 횟수: 값`

예시:
- 입력: `30\n25\n40\n10` → 누적 30→55→95→105, 105>100에서 종료
"""
# META_TESTS:
# - stdin: "30\n25\n40\n10"
#   expected_stdout: "누적합이 100을 초과했습니다!\n누적합: 105\n입력 횟수: 4"
# - stdin: "101"
#   expected_stdout: "누적합이 100을 초과했습니다!\n누적합: 101\n입력 횟수: 1"
# - stdin: "50\n51"
#   expected_stdout: "누적합이 100을 초과했습니다!\n누적합: 101\n입력 횟수: 2"

# while True + break를 사용하세요.
total = 0
count = 0
# TODO
