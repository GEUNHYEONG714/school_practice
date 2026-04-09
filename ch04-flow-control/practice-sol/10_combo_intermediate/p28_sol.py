"""
실습 28 풀이: 체스판 패턴
"""

n = int(input("크기 입력: "))

for i in range(n):
    for j in range(n):
        # 열 사이 공백 출력
        if j > 0:
            print(" ", end="")

        # 행 + 열의 합이 짝수이면 #, 홀수이면 .
        if (i + j) % 2 == 0:
            print("#", end="")
        else:
            print(".", end="")
    print()
