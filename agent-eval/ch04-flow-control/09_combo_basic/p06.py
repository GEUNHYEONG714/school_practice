"""
TITLE: 전기 요금 계산 (누진제)
DIFFICULTY: medium
TAGS: if, elif, else, arithmetic
EVAL: stdio

DESCRIPTION:
전기 사용량(kWh, 정수)을 입력받아 누진 요금을 계산하시오.

누진 요금:
- usage <= 100: usage * 60
- 100 < usage <= 200: 100*60 + (usage-100)*120
- usage > 200: 100*60 + 100*120 + (usage-200)*190

부가세는 `int(charge * 0.1)`, 총 납부 금액은 charge + tax.

출력 형식:
`전기 요금: 값원`
`부가세 (10%): 값원`
`총 납부 금액: 값원`

예시:
- 입력: `80` → 출력: `전기 요금: 4800원\n부가세 (10%): 480원\n총 납부 금액: 5280원`
- 입력: `250` → 출력: `전기 요금: 27500원\n부가세 (10%): 2750원\n총 납부 금액: 30250원`
"""
# META_TESTS:
# - stdin: "80"
#   expected_stdout: "전기 요금: 4800원\n부가세 (10%): 480원\n총 납부 금액: 5280원"
# - stdin: "250"
#   expected_stdout: "전기 요금: 27500원\n부가세 (10%): 2750원\n총 납부 금액: 30250원"
# - stdin: "150"
#   expected_stdout: "전기 요금: 12000원\n부가세 (10%): 1200원\n총 납부 금액: 13200원"

# 구간별로 나눠 계산하세요.
usage = int(input())
# TODO
