"""
실습 풀이: 다이아몬드
"""

n = int(input("크기를 입력하세요: "))

# 위쪽 삼각형 (1줄 ~ n줄)
for i in range(1, n + 1):
    # 공백 (n - i)개 출력
    for j in range(n - i):
        print(" ", end="")
    # 별 (2 * i - 1)개 출력
    for j in range(2 * i - 1):
        print("*", end="")
    print()  # 줄바꿈

# 아래쪽 역삼각형 (n-1줄 ~ 1줄)
for i in range(n - 1, 0, -1):
    # 공백 (n - i)개 출력
    for j in range(n - i):
        print(" ", end="")
    # 별 (2 * i - 1)개 출력
    for j in range(2 * i - 1):
        print("*", end="")
    print()  # 줄바꿈
