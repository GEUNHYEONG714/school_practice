"""
실습 87 풀이: 별 마름모
"""

n = int(input("홀수를 입력하세요: "))

mid = n // 2  # 가운데 줄 인덱스

for i in range(n):
    if i <= mid:
        # 윗부분: 별이 1, 3, 5, ... 개
        stars = 2 * i + 1
    else:
        # 아랫부분: 별이 줄어듦
        stars = 2 * (n - 1 - i) + 1

    # 앞 공백 계산
    spaces = (n - stars) // 2
    print(" " * spaces + "*" * stars)
