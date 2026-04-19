"""
실습 72 풀이: 계단 요금
"""

n = int(input("층수를 입력하세요: "))

total = 0

# 각 층의 요금과 누적 요금 출력
for k in range(1, n + 1):
    fee = k * 100
    total += fee
    print(str(k) + "층: " + str(fee) + "원 (누적: " + str(total) + "원)")
