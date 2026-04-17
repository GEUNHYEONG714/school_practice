"""
TITLE: 가격 할인 누적
DIFFICULTY: medium
TAGS: for, if, range, input, arithmetic, accumulator
EVAL: stdio

DESCRIPTION:
상품 개수 N을 입력받고, N개의 상품 가격을 차례로 입력받습니다.
10000원 이상인 상품만 20% 할인을 적용하고,
10000원 미만 상품은 원래 가격 그대로 합산합니다.

출력 형식:
- `총액: X원`

예시:
- 입력: `3\n15000\n8000\n20000` → 15000*0.8 + 8000 + 20000*0.8 = 12000+8000+16000 = 36000
- 출력: `총액: 36000원`
"""
# META_TESTS:
# - stdin: "3\n15000\n8000\n20000"
#   expected_stdout: "총액: 36000원"
# - stdin: "2\n5000\n3000"
#   expected_stdout: "총액: 8000원"
# - stdin: "1\n10000"
#   expected_stdout: "총액: 8000원"

# N개 상품 가격을 입력받아 조건부 할인 후 총액을 출력하세요.
n = int(input())
# TODO
