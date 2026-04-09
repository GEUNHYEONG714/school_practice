"""
실습 22 풀이: 숫자 다이아몬드
"""

n = int(input("높이(홀수) 입력: "))
mid = n // 2  # 가운데 줄 인덱스

for i in range(n):
    # 가운데로부터의 거리
    if i <= mid:
        dist = mid - i
    else:
        dist = i - mid

    # 해당 줄의 숫자 개수
    count = n - 2 * dist

    # 앞쪽 공백 출력
    for s in range(dist):
        print(" ", end="")

    # 1부터 증가했다가 감소하는 숫자 출력
    num = 0
    for j in range(count):
        if j < (count + 1) // 2:
            num += 1
        else:
            num -= 1
        print(num, end="")

    print()
