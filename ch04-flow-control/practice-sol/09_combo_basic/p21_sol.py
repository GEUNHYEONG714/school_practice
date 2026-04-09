"""
실습 풀이: 배수 합계
"""

n = int(input("N을 입력하세요: "))
m = int(input("M을 입력하세요: "))

total = 0  # 배수 합계

# 1부터 N까지 반복
for i in range(1, n + 1):
    # M으로 나눈 나머지가 0이면 M의 배수
    if i % m == 0:
        total += i

print("1부터 " + str(n) + "까지 " + str(m) + "의 배수의 합:", total)
