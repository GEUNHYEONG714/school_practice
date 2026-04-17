"""
TITLE: 체력 테스트 등급
DIFFICULTY: medium
TAGS: if, elif, comparison
EVAL: stdio

DESCRIPTION:
윗몸일으키기 횟수를 입력받아 체력 등급을 판정합니다.

등급 기준:
- 60회 이상: A
- 45회 이상: B
- 30회 이상: C
- 15회 이상: D
- 15회 미만: F

출력 형식: `횟수: N회 → 등급: X`

예시:
- 입력: `50` → 출력: `횟수: 50회 → 등급: B`
- 입력: `10` → 출력: `횟수: 10회 → 등급: F`
"""
# META_TESTS:
# - stdin: "50"
#   expected_stdout: "횟수: 50회 → 등급: B"
# - stdin: "60"
#   expected_stdout: "횟수: 60회 → 등급: A"
# - stdin: "10"
#   expected_stdout: "횟수: 10회 → 등급: F"

# 횟수에 따라 등급을 구분하세요
count = int(input())
# TODO
