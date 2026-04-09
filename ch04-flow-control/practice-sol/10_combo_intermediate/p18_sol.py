"""
실습 18 풀이: 친화수 찾기
"""

N = int(input("N을 입력하세요: "))

# 2부터 N까지 각 수에 대해 친화수 판별
a = 2
while a <= N:
    # a의 진약수 합 구하기
    sum_a = 1  # 1은 항상 진약수
    d = 2
    while d * d <= a:
        if a % d == 0:
            sum_a += d
            if d != a // d:  # 제곱근이 아닌 경우 짝 약수도 추가
                sum_a += a // d
        d += 1

    b = sum_a  # a의 진약수 합 = b

    # b가 a보다 크고 N 이하인 경우만 검사 (중복 출력 방지)
    if b > a and b <= N:
        # b의 진약수 합 구하기
        sum_b = 1
        d = 2
        while d * d <= b:
            if b % d == 0:
                sum_b += d
                if d != b // d:
                    sum_b += b // d
            d += 1

        # b의 진약수 합이 a이면 친화수 쌍
        if sum_b == a:
            print(f"({a}, {b})")

    a += 1
