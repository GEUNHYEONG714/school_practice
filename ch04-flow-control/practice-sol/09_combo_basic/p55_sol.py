"""
실습 55 풀이: 피자 주문 금액
"""

size = input("피자 사이즈를 입력하세요 (S/M/L): ")
qty = int(input("수량을 입력하세요: "))

# 사이즈별 단가 결정
if size == "S":
    price = 8000
elif size == "M":
    price = 12000
else:
    price = 15000

# 총액 계산
total = price * qty

# 3판 이상이면 10% 할인
print("사이즈: " + size + " | 수량: " + str(qty) + "판")
if qty >= 3:
    total = int(total * 0.9)
    print("총액: " + str(total) + "원")
    print("(10% 할인 적용)")
else:
    print("총액: " + str(total) + "원")
