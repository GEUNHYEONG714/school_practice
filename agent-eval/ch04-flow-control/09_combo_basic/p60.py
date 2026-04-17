"""
TITLE: 커피 포인트
DIFFICULTY: medium
TAGS: while, if, arithmetic, accumulation
EVAL: stdio

DESCRIPTION:
구매 횟수를 입력받은 뒤, 각 구매마다 음료 가격을 입력받아
총 적립 포인트와 스탬프 개수를 계산합니다.

규칙:
- 적립 포인트: 각 음료 가격의 5% (소수점 버림, 정수로 계산)
- 스탬프: 3잔마다 1개 (총 구매 잔수 // 3)

출력 형식:
- `총 구매: N잔`
- `총 적립 포인트: X점`
- `스탬프: Y개`

예시:
- 입력: `3\n4000\n5500\n3000` → 출력: `총 구매: 3잔\n총 적립 포인트: 625점\n스탬프: 1개`
"""
# META_TESTS:
# - stdin: "3\n4000\n5500\n3000"
#   expected_stdout: "총 구매: 3잔\n총 적립 포인트: 625점\n스탬프: 1개"
# - stdin: "1\n2000"
#   expected_stdout: "총 구매: 1잔\n총 적립 포인트: 100점\n스탬프: 0개"
# - stdin: "6\n1000\n2000\n3000\n4000\n5000\n6000"
#   expected_stdout: "총 구매: 6잔\n총 적립 포인트: 1050점\n스탬프: 2개"

# 반복문으로 각 음료 가격을 입력받아 포인트를 누적하세요
n = int(input())
# TODO
