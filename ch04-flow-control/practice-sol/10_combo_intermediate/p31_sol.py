"""
실습 31 풀이: ATM 시스템
"""

balance = 100000
withdraw_limit = 500000  # 1회 출금 한도

while True:
    print("===== ATM =====")
    print("1. 입금")
    print("2. 출금")
    print("3. 잔액조회")
    print("4. 종료")
    menu = int(input("메뉴 선택: "))

    if menu == 1:
        # 입금
        amount = int(input("입금액: "))
        if amount <= 0:
            print("입금액은 양수여야 합니다.")
        else:
            balance = balance + amount
            print(str(amount) + "원이 입금되었습니다.")
            print("현재 잔액: " + str(balance) + "원")

    elif menu == 2:
        # 출금
        amount = int(input("출금액: "))
        if amount <= 0:
            print("출금액은 양수여야 합니다.")
        elif amount > withdraw_limit:
            # 1회 출금 한도 초과
            print("1회 출금 한도(" + str(withdraw_limit) + "원)를 초과했습니다.")
        elif amount > balance:
            # 잔액 부족
            print("잔액이 부족합니다. 현재 잔액: " + str(balance) + "원")
        else:
            balance = balance - amount
            print(str(amount) + "원이 출금되었습니다.")
            print("현재 잔액: " + str(balance) + "원")

    elif menu == 3:
        # 잔액 조회
        print("현재 잔액: " + str(balance) + "원")

    elif menu == 4:
        # 종료
        print("이용해 주셔서 감사합니다.")
        break

    else:
        print("잘못된 메뉴입니다. 다시 선택해 주세요.")

    print()  # 메뉴 사이 빈 줄
