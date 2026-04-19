"""
실습 81 풀이: 자판기 (거스름돈)
"""
money = int(input())
price = int(input())

if money < price:
    print("잔액이 부족합니다.")
else:
    change = money - price
    print("거스름돈: " + str(change) + "원")

    if change > 0:
        # 500원
        c500 = change // 500
        change = change % 500
        if c500 > 0:
            print("500원: " + str(c500) + "개")

        # 100원
        c100 = change // 100
        change = change % 100
        if c100 > 0:
            print("100원: " + str(c100) + "개")

        # 50원
        c50 = change // 50
        change = change % 50
        if c50 > 0:
            print("50원: " + str(c50) + "개")

        # 10원
        c10 = change // 10
        if c10 > 0:
            print("10원: " + str(c10) + "개")
