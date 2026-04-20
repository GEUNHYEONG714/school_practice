"""
실습 37 풀이: 은행 대기번호 시스템
"""

last_issued = 0   # 마지막 발급 번호
last_called = 0   # 마지막 호출 번호

while True:
    print("===== 은행 대기번호 =====")
    print("1. 번호 발급")
    print("2. 다음 고객 호출")
    print("3. 대기인원 확인")
    print("4. 종료")
    menu = int(input("메뉴 선택: "))

    if menu == 1:
        # 번호 발급
        last_issued = last_issued + 1
        print("대기번호 " + str(last_issued) + "번이 발급되었습니다.")

    elif menu == 2:
        # 다음 고객 호출
        waiting = last_issued - last_called
        if waiting <= 0:
            print("대기 중인 고객이 없습니다.")
        else:
            last_called = last_called + 1
            # 창구 번호: 3개 창구를 순환 (첫 호출은 2번 창구부터 시작)
            window = (last_called % 3) + 1
            print(str(window) + "번 창구: " + str(last_called) + "번 고객님, 오세요!")

    elif menu == 3:
        # 대기인원 확인
        waiting = last_issued - last_called
        print("현재 대기인원: " + str(waiting) + "명")

    elif menu == 4:
        print("시스템을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다.")

    print()
