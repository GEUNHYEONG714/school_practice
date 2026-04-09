"""
실습 43 풀이: 자판기 시뮬레이션
"""

print("=== 자판기 ===")

while True:
    # 동전 투입
    money = int(input("동전 투입 (0: 종료): "))

    # 0원이면 종료
    if money == 0:
        print("이용해 주셔서 감사합니다!")
        break

    print("현재 잔액:", str(money) + "원")
    print("1.콜라(500원) 2.사이다(400원) 3.주스(700원)")

    # 음료 선택
    choice = int(input("음료 선택: "))

    # 음료 가격 결정
    price = 0
    name = ""

    if choice == 1:
        price = 500
        name = "콜라"
    elif choice == 2:
        price = 400
        name = "사이다"
    elif choice == 3:
        price = 700
        name = "주스"

    # 잔액 확인 후 구매 처리
    if money >= price:
        print(name + "를 구매했습니다!")
        money = money - price
    else:
        print("잔액이 부족합니다!")

    # 잔돈 반환
    print("잔돈:", str(money) + "원")
