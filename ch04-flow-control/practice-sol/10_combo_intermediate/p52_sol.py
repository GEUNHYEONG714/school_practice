"""
실습 52 풀이: 나르시시스트 수
"""

n = int(input("자릿수 N을 입력하세요: "))

# N자리 범위 설정
if n == 1:
    start = 1
else:
    start = 10 ** (n - 1)
end = 10 ** n

for i in range(start, end):
    # 각 자릿수의 N제곱 합 구하기
    power_sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        power_sum += digit ** n
        temp //= 10

    # 나르시시스트 수 판별
    if power_sum == i:
        print(i)
