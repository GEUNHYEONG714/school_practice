"""
실습 5 풀이: 직각삼각형 (오른쪽 정렬)
"""

n = int(input("줄 수를 입력하세요: "))

# 바깥 for문: 줄 번호 (1부터 n까지)
for i in range(1, n + 1):
    # 공백 출력: (n - i)개
    for j in range(n - i):
        print(" ", end="")
    # 별 출력: i개
    for j in range(i):
        print("*", end="")
    print()  # 줄바꿈
