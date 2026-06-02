"""
실습 24 풀이: 나비 모양 패턴

n=5 일 때 폭은 2n-1=9. 가운데 줄은 별이 9개 연속으로 채워진다.
양 끝 행으로 갈수록 좌/우 별 개수가 1개로 줄고 가운데 공백이 늘어난다.
"""

n = int(input("높이(홀수) 입력: "))
mid = n // 2     # 가운데 줄 인덱스
width = 2 * n - 1  # 한 줄의 전체 폭

for i in range(n):
    # 가운데 줄: 전체 폭만큼 별로 채움
    if i == mid:
        for j in range(width):
            print("*", end="")
        print()
        continue

    # 가운데로부터의 거리
    if i < mid:
        dist = mid - i
    else:
        dist = i - mid

    # 좌·우 별 개수 = mid - dist + 1, 가운데 공백 = width - 2*별
    side_stars = mid - dist + 1
    middle_space = width - 2 * side_stars

    # 좌측 별
    for j in range(side_stars):
        print("*", end="")
    # 가운데 공백
    for j in range(middle_space):
        print(" ", end="")
    # 우측 별
    for j in range(side_stars):
        print("*", end="")
    print()
