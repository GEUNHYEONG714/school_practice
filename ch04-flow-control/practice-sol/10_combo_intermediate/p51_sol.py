"""
실습 51 풀이: 하샤드 수
"""

n = int(input("N을 입력하세요: "))

for i in range(1, n + 1):
    # 자릿수 합 구하기
    digit_sum = 0
    temp = i
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    # 하샤드 수 판별
    if i % digit_sum == 0:
        print(i)
