"""
TITLE: 쇼핑 배송비 계산
DIFFICULTY: medium
TAGS: if, elif, else, calculation, string-comparison
EVAL: stdio

DESCRIPTION:
주문 금액(정수)과 회원 등급(문자열)을 순서대로 입력받아 배송비와 결제 금액을 출력하시오.

[배송비 규칙]
- 주문 금액 50000원 이상: 무료 배송 (배송비 0원)
- 주문 금액 30000원 이상: 배송비 2500원
- 주문 금액 30000원 미만: 배송비 5000원

[회원 할인]
- 등급이 `VIP`이면 배송비 50% 할인 (무료 배송인 경우 제외)
- 그 외 등급이면 할인 없음

최종 결제 금액 = 주문 금액 + 배송비
출력 형식: `배송비: ___원` 과 `결제 금액: ___원` 두 줄 출력

예시:
- 입력: `60000\n일반` → 출력: `배송비: 0원\n결제 금액: 60000원`
- 입력: `35000\nVIP` → 출력: `배송비: 1250원\n결제 금액: 36250원`
"""
# META_TESTS:
# - stdin: "60000\n일반"
#   expected_stdout: "배송비: 0원\n결제 금액: 60000원"
# - stdin: "35000\nVIP"
#   expected_stdout: "배송비: 1250원\n결제 금액: 36250원"
# - stdin: "20000\n일반"
#   expected_stdout: "배송비: 5000원\n결제 금액: 25000원"
# - stdin: "20000\nVIP"
#   expected_stdout: "배송비: 2500원\n결제 금액: 22500원"
# - stdin: "50000\nVIP"
#   expected_stdout: "배송비: 0원\n결제 금액: 50000원"

# 주문 금액과 회원 등급을 입력받아 배송비와 결제 금액을 출력하세요.
price = int(input())
grade = input()
# TODO
