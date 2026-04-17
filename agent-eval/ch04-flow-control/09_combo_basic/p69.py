"""
TITLE: 가격표 출력
DIFFICULTY: easy
TAGS: for, arithmetic, print
EVAL: stdio

DESCRIPTION:
단가와 수량범위 N을 입력받아 1개부터 N개까지의 가격표를 출력하시오.

출력 형식: `수량 x 단가 = 총액`

예시:
- 입력: `500\n3` → 단가 500원, 1~3개 가격표
"""
# META_TESTS:
# - stdin: "500\n3"
#   expected_stdout: "1 x 500 = 500\n2 x 500 = 1000\n3 x 500 = 1500"
# - stdin: "1200\n2"
#   expected_stdout: "1 x 1200 = 1200\n2 x 1200 = 2400"
# - stdin: "100\n5"
#   expected_stdout: "1 x 100 = 100\n2 x 100 = 200\n3 x 100 = 300\n4 x 100 = 400\n5 x 100 = 500"

# 단가와 수량범위 N을 입력받아 가격표를 출력하세요.
price = int(input())
n = int(input())
# TODO
