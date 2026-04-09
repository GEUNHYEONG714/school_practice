"""
실습 40 풀이: 마일리지 시스템
"""

mileage = 0        # 현재 보유 마일리지
total_earned = 0   # 총 적립
total_used = 0     # 총 사용
rate = 5           # 적립률 (%)

while True:
    print("===== 마일리지 시스템 =====")
    print("1. 구매 (마일리지 적립)")
    print("2. 마일리지 사용")
    print("3. 마일리지 조회")
    print("4. 종료")
    menu = int(input("메뉴 선택: "))

    if menu == 1:
        # 구매 → 마일리지 적립
        amount = int(input("구매 금액: "))
        if amount <= 0:
            print("구매 금액은 양수여야 합니다.")
        else:
            # 5% 적립 (소수점 이하 버림)
            earned = amount * rate // 100
            mileage = mileage + earned
            total_earned = total_earned + earned
            print(str(earned) + " 마일리지가 적립되었습니다!")

    elif menu == 2:
        # 마일리지 사용
        if mileage == 0:
            print("보유 마일리지가 없습니다.")
        else:
            use = int(input("사용할 마일리지: "))
            if use <= 0:
                print("1 이상의 값을 입력해 주세요.")
            elif use > mileage:
                # 보유 마일리지 부족
                print("마일리지가 부족합니다. (보유: " + str(mileage) + ")")
            else:
                mileage = mileage - use
                total_used = total_used + use
                print(str(use) + " 마일리지를 사용했습니다.")
                print("남은 마일리지: " + str(mileage))

    elif menu == 3:
        # 마일리지 조회
        print("보유 마일리지: " + str(mileage))
        print("총 적립: " + str(total_earned) + " / 총 사용: " + str(total_used))

    elif menu == 4:
        print("이용해 주셔서 감사합니다.")
        break

    else:
        print("잘못된 메뉴입니다.")

    print()
