"""
실습 79 풀이: 숫자 회전 사각형
"""
n = int(input())
layers = (n + 1) // 2  # 총 층 수

for r in range(n):
    line = ""
    for c in range(n):
        # (r, c)에서 가장 가까운 테두리까지 거리
        dist = r
        if c < dist:
            dist = c
        if (n - 1 - r) < dist:
            dist = n - 1 - r
        if (n - 1 - c) < dist:
            dist = n - 1 - c
        val = layers - dist  # 바깥쪽이 큰 수

        if c > 0:
            line += " "
        line += str(val)
    print(line)
