"""
실습 8 풀이: 역 숫자 피라미드
"""

n = int(input("줄 수를 입력하세요: "))

# 바깥 for문: 각 줄의 시작 숫자가 n, n-1, ..., 1로 줄어듦
for i in range(n, 0, -1):
    # 안쪽 for문: i부터 1까지 역순 출력
    for j in range(i, 0, -1):
        print(j, end="")
    print()  # 줄바꿈
