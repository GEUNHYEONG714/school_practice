"""
실습 10 풀이: 메뉴 주문 시스템
"""

total = 0  # 총 주문 금액

# 0을 입력할 때까지 무한 반복
while True:
    # 매 반복마다 메뉴판 출력
    print("--- 메뉴 ---")
    print("1. 아메리카노 (4000원)")
    print("2. 카페라떼 (4500원)")
    print("3. 녹차 (3500원)")
    print("0. 주문 완료")

    choice = int(input("메뉴를 선택하세요: "))

    # 선택한 메뉴에 따라 금액 누적
    if choice == 1:
        total += 4000
        print("아메리카노를 추가했습니다.")
    elif choice == 2:
        total += 4500
        print("카페라떼를 추가했습니다.")
    elif choice == 3:
        total += 3500
        print("녹차를 추가했습니다.")
    elif choice == 0:
        break  # 0 입력 시 주문 종료

# 반복이 끝난 후 총 금액 출력
print("총 주문 금액:", str(total) + "원")
