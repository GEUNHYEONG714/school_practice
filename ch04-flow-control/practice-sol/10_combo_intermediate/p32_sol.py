"""
실습 32 풀이: 도서관 대출 시스템
"""

borrowed = 0  # 현재 대출 권수
max_books = 5  # 최대 대출 가능 권수

while True:
    print("===== 도서관 대출 시스템 =====")
    print("1. 대출")
    print("2. 반납")
    print("3. 대출현황 조회")
    print("4. 종료")
    menu = int(input("메뉴 선택: "))

    if menu == 1:
        # 대출
        count = int(input("대출할 권수: "))
        if count <= 0:
            print("1권 이상 입력해 주세요.")
        elif borrowed + count > max_books:
            # 대출 한도 초과
            remain = max_books - borrowed
            print("대출 한도 초과! 추가 대출 가능 권수: " + str(remain) + "권")
        else:
            borrowed = borrowed + count
            print(str(count) + "권을 대출했습니다. (현재 대출: " + str(borrowed) + "권)")

    elif menu == 2:
        # 반납
        if borrowed == 0:
            print("현재 대출한 도서가 없습니다.")
        else:
            count = int(input("반납할 권수: "))
            if count <= 0:
                print("1권 이상 입력해 주세요.")
            elif count > borrowed:
                print("대출 권수보다 많이 반납할 수 없습니다. (현재 대출: " + str(borrowed) + "권)")
            else:
                borrowed = borrowed - count
                print(str(count) + "권을 반납했습니다. (현재 대출: " + str(borrowed) + "권)")

    elif menu == 3:
        # 대출현황 조회
        print("현재 대출 권수: " + str(borrowed) + "권")
        print("추가 대출 가능: " + str(max_books - borrowed) + "권")

    elif menu == 4:
        print("이용해 주셔서 감사합니다.")
        break

    else:
        print("잘못된 메뉴입니다. 다시 선택해 주세요.")

    print()
