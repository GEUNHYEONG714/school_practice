"""
실습 14 풀이: 간단한 메뉴 시스템
"""

# 무한 반복으로 메뉴를 계속 보여준다
while True:
    # 메뉴 출력
    print("===== 메뉴 =====")
    print("1. 인사")
    print("2. 날씨")
    print("q. 종료")
    print("================")

    choice = input("선택: ")

    # 사용자 입력에 따라 분기
    if choice == "1":
        print("안녕하세요!")
    elif choice == "2":
        print("오늘 날씨가 좋습니다!")
    elif choice == "q":
        print("프로그램을 종료합니다")
        break  # "q" 입력 시 반복 종료
    else:
        print("잘못된 입력입니다")
