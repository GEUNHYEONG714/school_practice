"""
실습 71 풀이: 숫자 나선 (반시계)
"""
n = int(input())
total = n * n
width = len(str(total))  # 가장 큰 수의 자릿수

# 방향: 아래(0), 오른쪽(1), 위(2), 왼쪽(3)
# 경계를 변수로 관리
top = 0
bottom = n - 1
left = 0
right = n - 1

num = 1
# 각 위치의 값을 직접 계산하여 출력
# 나선 순서대로 값을 채우되, 출력은 행/열 순서로 해야 하므로
# (r, c) 위치에 들어갈 숫자를 구하는 방식 사용
# 변수만 사용하므로 2중 루프에서 매번 나선을 따라가며 확인

for r in range(n):
    line = ""
    for c in range(n):
        # (r, c)에 들어갈 숫자를 나선 순서로 계산
        # 바깥 껍질부터 몇 번째 껍질인지 계산
        layer = r
        if c < layer:
            layer = c
        if (n - 1 - r) < layer:
            layer = n - 1 - r
        if (n - 1 - c) < layer:
            layer = n - 1 - c

        # 이 껍질 시작 전까지 채워진 숫자 개수
        prev = 0
        k = 0
        while k < layer:
            prev += 4 * (n - 1 - 2 * k)
            k += 1

        # 현재 껍질의 크기
        side = n - 2 * layer

        if side == 1:
            val = prev + 1
        else:
            # 반시계: 아래 → 오른쪽 → 위 → 왼쪽
            # 아래: (layer, layer) → (layer+side-1, layer)
            if c == layer and r >= layer and r <= layer + side - 1:
                val = prev + (r - layer) + 1
            # 오른쪽: (layer+side-1, layer+1) → (layer+side-1, layer+side-1)
            elif r == layer + side - 1 and c > layer and c <= layer + side - 1:
                val = prev + (side - 1) + (c - layer)
            # 위: (layer+side-2, layer+side-1) → (layer, layer+side-1)
            elif c == layer + side - 1 and r >= layer and r < layer + side - 1:
                val = prev + 2 * (side - 1) + (layer + side - 1 - r)
            # 왼쪽: (layer, layer+side-2) → (layer, layer+1)
            elif r == layer and c > layer and c < layer + side - 1:
                val = prev + 3 * (side - 1) + (layer + side - 1 - c)
            else:
                val = 0

        if c > 0:
            line += " "
        # 오른쪽 정렬
        s = str(val)
        while len(s) < width:
            s = " " + s
        line += s
    print(line)
