"""
실습 78 풀이: 테두리 삼각형
"""
n = int(input())

for i in range(1, n + 1):
    if i == 1:
        # 꼭대기: 공백 + 별 1개
        line = ""
        for s in range(n - 1):
            line += " "
        line += "*"
        print(line)
    elif i == n:
        # 밑변: 별 2*N-1개
        line = ""
        for s in range(2 * n - 1):
            line += "*"
        print(line)
    else:
        # 중간: 양쪽 끝에만 별
        line = ""
        for s in range(n - i):
            line += " "
        line += "*"
        inner = 2 * i - 3  # 안쪽 공백 수
        for s in range(inner):
            line += " "
        line += "*"
        print(line)
