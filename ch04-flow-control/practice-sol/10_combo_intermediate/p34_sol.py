"""
실습 34 풀이: 편의점 계산기
"""

# 상품 가격
price1 = 1200   # 삼각김밥
price2 = 1500   # 음료수
price3 = 2000   # 과자

# 각 상품별 구매 수량
qty1 = 0
qty2 = 0
qty3 = 0

while True:
    print("===== 편의점 =====")
    print("1. 삼각김밥 (" + str(price1) + "원)")
    print("2. 음료수 (" + str(price2) + "원)")
    print("3. 과자 (" + str(price3) + "원)")
    item = int(input("상품 번호: "))

    if item == 1:
        count = int(input("수량: "))
        qty1 = qty1 + count
        print("삼각김밥 " + str(count) + "개 추가!")
    elif item == 2:
        count = int(input("수량: "))
        qty2 = qty2 + count
        print("음료수 " + str(count) + "개 추가!")
    elif item == 3:
        count = int(input("수량: "))
        qty3 = qty3 + count
        print("과자 " + str(count) + "개 추가!")
    else:
        print("잘못된 상품 번호입니다.")
        continue

    # 계속 쇼핑 여부
    again = int(input("계속 쇼핑하시겠습니까? (1:예 / 2:아니오): "))
    if again != 1:
        break
    print()

# 계산서 출력
print()
print("===== 계산서 =====")
total = 0

if qty1 > 0:
    sub = qty1 * price1
    print("삼각김밥 x " + str(qty1) + " = " + str(sub) + "원")
    total = total + sub

if qty2 > 0:
    sub = qty2 * price2
    print("음료수 x " + str(qty2) + " = " + str(sub) + "원")
    total = total + sub

if qty3 > 0:
    sub = qty3 * price3
    print("과자 x " + str(qty3) + " = " + str(sub) + "원")
    total = total + sub

print("총액: " + str(total) + "원")
