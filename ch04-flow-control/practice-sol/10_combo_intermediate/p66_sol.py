"""
실습 66 풀이: 동전 거스름돈 (최소 개수)
"""

money = int(input("거스름돈을 입력하세요: "))

total_coins = 0

# 500원
cnt500 = money // 500
money %= 500
print(f"500원: {cnt500}개")
total_coins += cnt500

# 100원
cnt100 = money // 100
money %= 100
print(f"100원: {cnt100}개")
total_coins += cnt100

# 50원
cnt50 = money // 50
money %= 50
print(f"50원: {cnt50}개")
total_coins += cnt50

# 10원
cnt10 = money // 10
print(f"10원: {cnt10}개")
total_coins += cnt10

print(f"총 동전 수: {total_coins}개")
