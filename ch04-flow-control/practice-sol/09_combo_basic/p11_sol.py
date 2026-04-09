"""
실습 11 풀이: 환전 프로그램
"""

print("=== 환전 프로그램 ===")
print("1. 달러 (USD)")
print("2. 엔 (JPY)")
print("3. 유로 (EUR)")
currency = int(input("통화를 선택하세요 (1/2/3): "))
krw = int(input("환전할 원화 금액을 입력하세요: "))

# 통화별 환전 계산
if currency == 1:
    # 달러: 1달러 = 1350원
    result = krw / 1350
    print("환전 금액:", round(result, 2), "달러")
elif currency == 2:
    # 엔: 100엔 = 900원 → 1엔 = 9원
    result = krw / 9
    print("환전 금액:", round(result, 2), "엔")
elif currency == 3:
    # 유로: 1유로 = 1450원
    result = krw / 1450
    print("환전 금액:", round(result, 2), "유로")
else:
    print("잘못된 통화 선택입니다.")

# 유효한 통화를 선택한 경우에만 수수료 출력
if currency >= 1 and currency <= 3:
    # 수수료 1.5%
    fee = int(krw * 0.015)
    print("수수료 (1.5%):", str(fee) + "원")
    total = krw + fee
    print("실 지불 금액:", str(total) + "원")
