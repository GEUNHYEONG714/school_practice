"""
실습 10 풀이: 곱셈표
"""

# 헤더 출력: X  1  2  3  4  5
print("X", end="\t")
for i in range(1, 6):
    print(i, end="\t")
print()  # 줄바꿈

# 구분선 출력
print("-" * 30)

# 곱셈표 본문
# 바깥 for문: 행 (1 ~ 5)
for i in range(1, 6):
    # 행 번호 출력
    print(i, end="\t")
    # 안쪽 for문: 열 (1 ~ 5)
    for j in range(1, 6):
        print(i * j, end="\t")
    print()  # 줄바꿈
