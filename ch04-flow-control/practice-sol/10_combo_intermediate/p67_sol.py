"""
실습 67 풀이: 최대 직사각형
"""

n = int(input("N을 입력하세요: "))
heights = input("높이를 입력하세요: ")

parts = heights.split()
max_area = 0

# 이중 for문: 모든 시작~끝 구간
for i in range(n):
    min_height = None
    for j in range(i, n):
        # j번째 높이 구하기 (인덱스로 접근)
        idx = 0
        for p in parts:
            if idx == j:
                h = int(p)
                break
            idx += 1

        # 구간 내 최소 높이 갱신
        if min_height is None or h < min_height:
            min_height = h

        # 넓이 계산
        area = min_height * (j - i + 1)
        if area > max_area:
            max_area = area

print(max_area)
