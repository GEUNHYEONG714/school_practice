"""
실습 25 풀이: 빈 다이아몬드
"""

n = int(input("높이(홀수) 입력: "))
mid = n // 2  # 가운데 줄 인덱스

for i in range(n):
    # 가운데로부터의 거리
    if i <= mid:
        dist = mid - i
    else:
        dist = i - mid

    # 해당 줄의 별 영역 너비
    width = n - 2 * dist

    # 앞쪽 공백 출력
    for s in range(dist):
        print(" ", end="")

    # 별이 1개인 줄 (꼭짓점)
    if width == 1:
        print("*")
    else:
        # 첫 번째 별
        print("*", end="")
        # 안쪽 공백
        for s in range(width - 2):
            print(" ", end="")
        # 마지막 별
        print("*")
