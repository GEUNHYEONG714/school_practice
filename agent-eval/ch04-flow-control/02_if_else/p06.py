"""
TITLE: 온라인 쇼핑 재고 확인
DIFFICULTY: easy
TAGS: if, else, comparison, print

EVAL: stdio

DESCRIPTION:
상품 재고 수량을 입력받아 아래 규칙에 따라 출력하시오.

- 재고가 0이면 두 줄 출력: `품절입니다`, `입고 예정입니다`
- 재고가 0이 아니면 한 줄 출력: `구매 가능합니다`
- 어떤 경우든 마지막에는 `쇼핑을 계속합니다`를 출력

예시:
- 입력: `0` → 출력: `품절입니다\n입고 예정입니다\n쇼핑을 계속합니다`
- 입력: `5` → 출력: `구매 가능합니다\n쇼핑을 계속합니다`
"""
# META_TESTS:
# - stdin: "0"
#   expected_stdout: "품절입니다\n입고 예정입니다\n쇼핑을 계속합니다"
# - stdin: "5"
#   expected_stdout: "구매 가능합니다\n쇼핑을 계속합니다"

# if/else 블록 안과 블록 밖의 들여쓰기 차이에 주의하세요.
stock = int(input())
# TODO
