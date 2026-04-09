"""
실습 11 풀이: 쌍둥이 소수 찾기
"""

N = int(input("N을 입력하세요: "))

# 2부터 N-2까지 각 수에 대해 검사
num = 2
while num <= N - 2:
    # num이 소수인지 판별
    is_prime1 = True
    if num < 2:
        is_prime1 = False
    else:
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                is_prime1 = False
                break
            divisor += 1

    # num + 2가 소수인지 판별
    is_prime2 = True
    pair = num + 2
    if pair < 2:
        is_prime2 = False
    else:
        divisor = 2
        while divisor * divisor <= pair:
            if pair % divisor == 0:
                is_prime2 = False
                break
            divisor += 1

    # 둘 다 소수이면 쌍둥이 소수 출력
    if is_prime1 and is_prime2 and pair <= N:
        print(f"({num}, {pair})")

    num += 1
