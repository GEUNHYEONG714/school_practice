"""
실습 15 풀이: 해밍수 찾기
"""

N = int(input("N을 입력하세요: "))

# 1부터 N까지 각 수에 대해 해밍수 판별
num = 1
while num <= N:
    temp = num  # 원본 보존을 위해 임시 변수 사용

    # 2로 나눌 수 있을 때까지 나누기
    while temp % 2 == 0:
        temp //= 2

    # 3으로 나눌 수 있을 때까지 나누기
    while temp % 3 == 0:
        temp //= 3

    # 5로 나눌 수 있을 때까지 나누기
    while temp % 5 == 0:
        temp //= 5

    # 2, 3, 5로 모두 나눈 결과가 1이면 해밍수
    if temp == 1:
        print(num)

    num += 1
