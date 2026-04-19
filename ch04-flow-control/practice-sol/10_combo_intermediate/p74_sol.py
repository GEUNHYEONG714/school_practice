"""
실습 74 풀이: 빈 사각형 (대각선 포함)
"""
n = int(input())

for r in range(n):
    # 마지막 *의 열 위치를 먼저 계산
    last_star = 0
    for c in range(n):
        is_star = 0
        # 테두리
        if r == 0 or r == n - 1 or c == 0 or c == n - 1:
            is_star = 1
        # 주대각선
        if r == c:
            is_star = 1
        # 부대각선
        if r + c == n - 1:
            is_star = 1
        if is_star == 1:
            last_star = c

    # 출력
    line = ""
    for c in range(last_star + 1):
        is_star = 0
        if r == 0 or r == n - 1 or c == 0 or c == n - 1:
            is_star = 1
        if r == c:
            is_star = 1
        if r + c == n - 1:
            is_star = 1

        if is_star == 1:
            line += "*"
        else:
            line += " "
    print(line)
