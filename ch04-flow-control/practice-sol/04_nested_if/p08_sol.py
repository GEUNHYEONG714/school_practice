"""
실습 풀이: 주문 처리
"""

order_type = input("주문 방식을 입력하세요 (배달/포장): ")
price = 15000

# 바깥 if/elif/else: 주문 방식 분기
if order_type == "배달":
    distance = float(input("거리를 입력하세요(km): "))
    # 안쪽 if: 거리에 따라 배달비 결정
    if distance <= 3:
        delivery_fee = 2000
    else:
        delivery_fee = 3500
    total = price + delivery_fee
    print("배달 주문: 음식", str(price) + "원", "+", "배달비", str(delivery_fee) + "원", "=", "총", str(total) + "원")
elif order_type == "포장":
    # 포장은 고정 할인
    discount = 2000
    total = price - discount
    print("포장 주문: 음식", str(price) + "원", "-", "할인", str(discount) + "원", "=", "총", str(total) + "원")
else:
    print("잘못된 주문 방식입니다.")
