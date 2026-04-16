"""
TITLE: 중고차 가격 산정
DIFFICULTY: medium
TAGS: if, elif, else, arithmetic
EVAL: stdio

DESCRIPTION:
신차 가격(만원, 정수), 연식(년, 정수), 주행거리(만 km, 실수), 사고 유무(Y/N, 문자열)를 각각 한 줄씩 입력받아 중고차 가격을 산정하시오.

연식 감가율(%):
- year <= 3: year * 10
- year <= 7: 3*10 + (year-3)*7
- year > 7: 3*10 + 4*7 + (year-7)*5

주행거리 감가율(%):
- km <= 5: 0
- km <= 10: 5
- km > 10: 10

사고 감가율(%): Y 또는 y면 15, 아니면 0.

총 감가율 = 세 감가율 합.
최종 가격 = `int(new_price * (1 - total_discount/100))`
최소 가격 = `int(new_price * 0.1)`; 최종 가격이 최소보다 작으면 최소 가격으로.

출력 형식 (5줄):
`--- 감가 내역 ---`
`연식 감가 (year년): X%`
`주행거리 감가: X%`
`사고 감가: X%`
`총 감가율: X%`
`예상 중고차 가격: 값만원`

예시:
- 입력: `3000\n5\n8\nN` → 총 감가율 49%, 예상 1530만원
"""
# META_TESTS:
# - stdin: "3000\n5\n8\nN"
#   expected_stdout: "--- 감가 내역 ---\n연식 감가 (5년): 44%\n주행거리 감가: 5%\n사고 감가: 0%\n총 감가율: 49%\n예상 중고차 가격: 1530만원"
# - stdin: "2000\n10\n15\nY"
#   expected_stdout: "--- 감가 내역 ---\n연식 감가 (10년): 59%\n주행거리 감가: 10%\n사고 감가: 15%\n총 감가율: 84%\n예상 중고차 가격: 320만원"

# 각 감가율을 따로 계산한 뒤 합산하고 최저가를 체크하세요.
new_price = int(input())
year = int(input())
km = float(input())
accident = input()
# TODO
