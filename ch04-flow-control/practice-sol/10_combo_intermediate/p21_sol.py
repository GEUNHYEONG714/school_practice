"""
실습 21 풀이: 모래시계 패턴
"""

n = int(input("높이(홀수) 입력: "))
mid = n // 2  # 가운데 줄 인덱스

# 위쪽 역삼각형 (가운데 포함)
for i in range(mid + 1):
    # 공백 출력
    for s in range(i):
        print(" ", end="")
    # 별 출력
    for j in range(n - 2 * i):
        print("*", end="")
    print()

# 아래쪽 삼각형 (가운데 제외)
for i in range(mid - 1, -1, -1):
    # 공백 출력
    for s in range(i):
        print(" ", end="")
    # 별 출력
    for j in range(n - 2 * i):
        print("*", end="")
    print()
