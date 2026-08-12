"""
실습 7: 할인 가격 계산

아래 3개 상품의 원래 가격과 할인율이 주어져 있습니다.
각 상품의 할인 가격을 계산하고, 총 결제 금액을 구하세요.

힌트: 할인 가격 = 원래 가격 * (1 - 할인율)
      총액은 += 연산자로 누적합니다.
"""

total = 0

# 상품 1: 노트북 1200000원, 10% 할인
price1 = 1200000
discount1 = price1 * 0.1
total += price1 - discount1

# 상품 2: 마우스 35000원, 20% 할인
price2 = 35000
discount2 = price2 * 0.2
total += price2 - discount2

# 상품 3: 키보드 55000원, 15% 할인
price3 = 55000
discount3 = price3 * 0.15
total += price3 - discount3

# 아래에 각 상품의 할인 가격을 계산하고 총액을 구하세요
print(f"노트북: {price1 - discount1:.0f}원")
print(f"마우스: {price2 - discount2:.0f}원")
print(f"키보드: {price3 - discount3:.0f}원")
print(f"총 결제 금액: {total:.0f}원")


"""
[실행 결과 예시]
노트북: 1080000원
마우스: 28000원
키보드: 46750원
총 결제 금액: 1154750원
"""
