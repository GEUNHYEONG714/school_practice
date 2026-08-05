"""
실습 2: 거스름돈 계산

물건 가격과 지불 금액을 입력받아 거스름돈을 계산하세요.
거스름돈은 1000원, 500원, 100원 단위로 나눠서 출력합니다.

힌트: //(몫)과 %(나머지)를 활용하세요.
"""

price = int(input("물건 가격: "))
paid = int(input("지불 금액: "))

change = paid - price

# 아래에 1000원, 500원, 100원 개수를 계산하여 출력하세요
print("거스름돈:", str(change) + "원")
thousand = change // 1000
change = change % 1000
five_hundred = change // 500
change = change % 500
hundred = change // 100
print("1000원:", thousand, "개")
print("500원:", five_hundred, "개")
print("100원:", hundred, "개")

"""
[실행 결과 예시] (입력: 2300, 5000)
거스름돈: 2700원
1000원: 2개
500원: 1개
100원: 2개
"""
