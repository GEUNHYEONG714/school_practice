"""
실습 12 풀이: 골드바흐의 추측
"""

N = int(input("짝수를 입력하세요: "))

# 2부터 N//2까지 반복
i = 2
while i <= N // 2:
    # i가 소수인지 판별
    is_prime_i = True
    if i < 2:
        is_prime_i = False
    else:
        d = 2
        while d * d <= i:
            if i % d == 0:
                is_prime_i = False
                break
            d += 1

    # N - i가 소수인지 판별
    j = N - i
    is_prime_j = True
    if j < 2:
        is_prime_j = False
    else:
        d = 2
        while d * d <= j:
            if j % d == 0:
                is_prime_j = False
                break
            d += 1

    # 둘 다 소수이면 출력
    if is_prime_i and is_prime_j:
        print(f"{N} = {i} + {j}")

    i += 1
