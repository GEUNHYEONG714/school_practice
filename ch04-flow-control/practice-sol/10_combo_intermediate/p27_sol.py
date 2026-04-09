"""
실습 27 풀이: X자 패턴
"""

n = int(input("크기 입력: "))

for i in range(n):
    for j in range(n):
        # 주대각선 또는 부대각선 위치이면 별 출력
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
