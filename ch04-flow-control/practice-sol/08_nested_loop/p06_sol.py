"""
실습 6 풀이: 사각형 테두리
"""

n = int(input("크기를 입력하세요: "))

# 바깥 for문: 행 (0 ~ n-1)
for i in range(n):
    # 안쪽 for문: 열 (0 ~ n-1)
    for j in range(n):
        # 테두리 조건: 첫/마지막 행 또는 첫/마지막 열
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # 줄바꿈
