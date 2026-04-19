"""
실습 90 풀이: 가격 할인 누적
"""

n = int(input("상품 개수: "))
total = 0

for i in range(n):
    price = int(input("상품 가격: "))

    # 10000원 이상이면 20% 할인 적용
    if price >= 10000:
        total += int(price * 0.8)
    else:
        total += price

print("총액: " + str(total) + "원")
