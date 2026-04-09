"""
실습 4 풀이: 역삼각형 별 찍기
"""

n = int(input("줄 수를 입력하세요: "))

# 바깥 for문: 줄마다 별 개수가 n, n-1, ..., 1로 줄어듦
for i in range(n, 0, -1):
    # 안쪽 for문: 해당 줄에 별 i개 출력
    for j in range(i):
        print("*", end="")
    print()  # 줄바꿈
