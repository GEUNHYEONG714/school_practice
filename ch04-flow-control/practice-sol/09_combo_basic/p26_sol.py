"""
실습 26 풀이: 음료 자판기
"""

money = int(input("투입 금액을 입력하세요: "))

# 잔액이 가장 싼 음료(500원)보다 적으면 종료
while money >= 500:
    print("잔액:", str(money) + "원")
    print("1. 물 (500원)")
    print("2. 주스 (1000원)")
    print("3. 커피 (1500원)")

    choice = int(input("음료를 선택하세요: "))

    # 선택한 음료의 가격과 안내 문구 확인 (조사 주의: 물→을, 주스/커피→를)
    if choice == 1:
        price = 500
        message = "물을 선택했습니다."
    elif choice == 2:
        price = 1000
        message = "주스를 선택했습니다."
    elif choice == 3:
        price = 1500
        message = "커피를 선택했습니다."
    else:
        print("잘못된 선택입니다.")
        continue  # 다시 선택

    # 잔액 부족 여부 확인
    if money >= price:
        money -= price
        print(message)
    else:
        print("잔액이 부족합니다.")
        break

print("남은 금액:", str(money) + "원")
