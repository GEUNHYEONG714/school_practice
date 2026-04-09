"""
실습 30 풀이: 숫자 테두리 사각형
"""

n = int(input("크기 입력: "))

for i in range(n):
    for j in range(n):
        # 열 사이 공백 출력
        if j > 0:
            print(" ", end="")

        # 가장 가까운 가장자리까지의 거리 + 1이 값
        # 위, 아래, 왼쪽, 오른쪽 테두리까지의 거리 중 최솟값
        dist = i
        if j < dist:
            dist = j
        if (n - 1 - i) < dist:
            dist = n - 1 - i
        if (n - 1 - j) < dist:
            dist = n - 1 - j

        print(dist + 1, end="")

    print()
