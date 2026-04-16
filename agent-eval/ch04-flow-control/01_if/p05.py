"""
TITLE: 잔액 부족 알림
DIFFICULTY: easy
TAGS: if, comparison, print
EVAL: stdio

DESCRIPTION:
커피 가격과 내 잔액을 순서대로 입력받아,
잔액이 가격보다 적으면 `잔액이 부족합니다`를 출력하시오.
잔액이 충분하면 아무것도 출력하지 마시오.

예시:
- 입력: `4500\n3000` → 출력: `잔액이 부족합니다`
- 입력: `3000\n5000` → 출력: (없음)
- 입력: `4500\n4500` → 출력: (없음)
"""
# META_TESTS:
# - stdin: "4500\n3000"
#   expected_stdout: "잔액이 부족합니다"
# - stdin: "3000\n5000"
#   expected_stdout: ""
# - stdin: "4500\n4500"
#   expected_stdout: ""

# 잔액이 가격보다 적으면 "잔액이 부족합니다"를 출력하세요.
price = int(input())
balance = int(input())
# TODO
