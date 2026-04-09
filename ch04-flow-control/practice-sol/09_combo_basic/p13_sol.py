"""
실습 풀이: 1~N 합계
"""

n = int(input("N을 입력하세요: "))

total = 0  # 합계를 저장할 변수

# 1부터 N까지 반복하며 누적
for i in range(1, n + 1):
    total += i

print("1부터 " + str(n) + "까지의 합:", total)
