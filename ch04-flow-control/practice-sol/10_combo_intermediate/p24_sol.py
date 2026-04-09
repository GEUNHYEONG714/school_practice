"""
실습 24 풀이: 나비 모양 패턴
"""

n = int(input("높이(홀수) 입력: "))
mid = n // 2  # 가운데 줄 인덱스

for i in range(n):
    # 가운데로부터의 거리 계산
    if i <= mid:
        dist = mid - i
    else:
        dist = i - mid

    # 왼쪽 별 개수 = mid - dist + 1
    left_stars = mid - dist + 1
    # 가운데 공백 = n - 2 * left_stars (가운데 줄에서는 0)
    middle_space = n - 2 * left_stars

    # 왼쪽 별 출력
    for j in range(left_stars):
        print("*", end="")

    # 가운데 공백 출력
    for j in range(middle_space):
        print(" ", end="")

    # 오른쪽 별 출력 (가운데 줄이 아닌 경우)
    if middle_space > 0:
        for j in range(left_stars):
            print("*", end="")

    print()
