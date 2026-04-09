"""
실습 33 풀이: 주차장 관리 시스템
"""

parked = 0        # 현재 주차 대수
max_cars = 10     # 최대 주차 가능 대수
total_income = 0  # 총 수입
rate = 1000       # 시간당 요금

while True:
    print("===== 주차장 관리 =====")
    print("1. 입차")
    print("2. 출차")
    print("3. 현황 조회")
    print("4. 종료")
    menu = int(input("메뉴 선택: "))

    if menu == 1:
        # 입차
        if parked >= max_cars:
            print("주차장이 만차입니다!")
        else:
            parked = parked + 1
            print("차량이 입차되었습니다. (현재 주차: " + str(parked) + "/" + str(max_cars) + "대)")

    elif menu == 2:
        # 출차
        if parked <= 0:
            print("주차된 차량이 없습니다.")
        else:
            hours = int(input("주차 시간(시간 단위): "))
            # 1시간 미만(0시간)은 무료
            if hours <= 0:
                fee = 0
            else:
                fee = hours * rate
            print("주차 요금: " + str(fee) + "원")
            total_income = total_income + fee
            parked = parked - 1
            print("차량이 출차되었습니다. (현재 주차: " + str(parked) + "/" + str(max_cars) + "대)")

    elif menu == 3:
        # 현황 조회
        empty = max_cars - parked
        print("현재 주차: " + str(parked) + "/" + str(max_cars) + "대")
        print("빈 자리: " + str(empty) + "대")
        print("총 수입: " + str(total_income) + "원")

    elif menu == 4:
        print("시스템을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다.")

    print()
