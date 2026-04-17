"""
TITLE: 피자 주문 금액
DIFFICULTY: medium
TAGS: if, elif, arithmetic, comparison
EVAL: stdio

DESCRIPTION:
피자 사이즈(S/M/L)와 수량을 입력받아 총 금액을 계산합니다.

사이즈별 가격:
- S: 8000원
- M: 12000원
- L: 15000원

할인: 3판 이상 주문 시 총액에서 10% 할인

출력 형식:
- `사이즈: X | 수량: N판`
- `총액: X원`
- 할인 적용 시 추가: `(10% 할인 적용)`

예시:
- 입력: `M\n2` → 출력: `사이즈: M | 수량: 2판\n총액: 24000원`
- 입력: `L\n3` → 출력: `사이즈: L | 수량: 3판\n총액: 40500원\n(10% 할인 적용)`
"""
# META_TESTS:
# - stdin: "M\n2"
#   expected_stdout: "사이즈: M | 수량: 2판\n총액: 24000원"
# - stdin: "L\n3"
#   expected_stdout: "사이즈: L | 수량: 3판\n총액: 40500원\n(10% 할인 적용)"
# - stdin: "S\n5"
#   expected_stdout: "사이즈: S | 수량: 5판\n총액: 36000원\n(10% 할인 적용)"

# 사이즈별 단가를 정하고, 3판 이상이면 10% 할인
size = input()
qty = int(input())
# TODO
