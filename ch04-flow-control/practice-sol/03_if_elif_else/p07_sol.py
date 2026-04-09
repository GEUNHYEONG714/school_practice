"""
실습 8 풀이: 동전 변환
"""

amount = int(input("금액을 입력하세요 (원): "))

# 큰 동전부터 계산하고 나머지를 다음 동전에 넘긴다
coin500 = amount // 500
remainder = amount % 500

coin100 = remainder // 100
remainder = remainder % 100

coin50 = remainder // 50
remainder = remainder % 50

coin10 = remainder // 10

total = coin500 + coin100 + coin50 + coin10

print(str(amount) + "원 → 동전 변환:")
print("500원: " + str(coin500) + "개")
print("100원: " + str(coin100) + "개")
print("50원: " + str(coin50) + "개")
print("10원: " + str(coin10) + "개")
print("총 동전 수: " + str(total) + "개")
