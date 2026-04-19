"""
실습 60 풀이: 커피 포인트
"""

n = int(input("구매 횟수를 입력하세요: "))

total_point = 0
i = 0

# 각 음료 가격을 입력받아 포인트 누적
while i < n:
    price = int(input("음료 가격을 입력하세요: "))
    total_point += price * 5 // 100
    i += 1

# 스탬프: 3잔마다 1개
stamp = n // 3

print("총 구매: " + str(n) + "잔")
print("총 적립 포인트: " + str(total_point) + "점")
print("스탬프: " + str(stamp) + "개")
