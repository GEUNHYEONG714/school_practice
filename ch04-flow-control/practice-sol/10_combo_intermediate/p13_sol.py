"""
실습 13 풀이: 두 수의 합 (Two Sum)
"""

N = int(input("N을 입력하세요: "))
target = int(input("target을 입력하세요: "))

# 1부터 N까지 이중 반복으로 쌍 탐색
a = 1
while a <= N:
    b = a + 1  # a보다 큰 수부터 시작 (중복 방지)
    while b <= N:
        # 두 수의 합이 target과 같으면 출력
        if a + b == target:
            print(f"({a}, {b})")
        b += 1
    a += 1
