"""
실습 72 풀이: 별 화살표
"""
n = int(input())

# 총 2*N-1 행 출력
for i in range(1, 2 * n):
    # 위쪽 절반: i개, 아래쪽 절반: 2*n-i개
    if i <= n:
        count = i
    else:
        count = 2 * n - i

    line = ""
    for j in range(count):
        if j > 0:
            line += " "
        line += "*"
    print(line)
