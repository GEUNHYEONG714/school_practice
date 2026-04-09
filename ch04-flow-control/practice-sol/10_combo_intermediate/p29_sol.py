"""
실습 29 풀이: 나선형 숫자 (어려움)

리스트 없이 변수만 사용합니다.
각 위치 (r, c)에 대해 해당 위치의 나선형 값을 직접 계산합니다.
바깥 테두리 층(layer)을 구한 뒤, 그 층에서의 위치로 값을 구합니다.
"""

n = int(input("크기 입력: "))

for r in range(n):
    for c in range(n):
        # 현재 위치의 층(layer) 계산: 가장 가까운 가장자리까지의 거리
        layer = r
        if c < layer:
            layer = c
        if (n - 1 - r) < layer:
            layer = n - 1 - r
        if (n - 1 - c) < layer:
            layer = n - 1 - c

        # 이 층 이전까지 채워진 숫자 개수
        # 바깥 layer개 테두리의 총 칸 수 = 4 * layer * (n - layer) - 4 * layer * layer
        # 간단히: 각 테두리 k의 칸 수 = 4 * (n - 2*k - 1)
        prev = 0
        for k in range(layer):
            prev = prev + 4 * (n - 2 * k - 1)

        # 현재 층의 크기
        side = n - 2 * layer

        # 현재 층 내에서의 위치 계산 (시계 방향)
        # 상단 행: 왼 -> 오
        if r == layer:
            pos = c - layer
        # 우측 열: 위 -> 아래
        elif c == layer + side - 1:
            pos = side - 1 + (r - layer)
        # 하단 행: 오 -> 왼
        elif r == layer + side - 1:
            pos = side - 1 + side - 1 + (layer + side - 1 - c)
        # 좌측 열: 아래 -> 위
        else:
            pos = side - 1 + side - 1 + side - 1 + (layer + side - 1 - r)

        val = prev + pos + 1

        # 자릿수 맞춰 출력
        if c > 0:
            print(" ", end="")
        # 숫자를 너비에 맞춰 출력
        width = len(str(n * n))
        num_str = str(val)
        # 앞에 공백 추가하여 오른쪽 정렬
        while len(num_str) < width:
            num_str = " " + num_str
        print(num_str, end="")

    print()
