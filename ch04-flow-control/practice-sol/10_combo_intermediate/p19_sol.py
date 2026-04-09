"""
실습 19 풀이: 교대 수열의 합
"""

N = int(input("항의 수를 입력하세요: "))

total = 0.0  # 누적 합
i = 1

while i <= N:
    # 홀수 번째 항은 더하고, 짝수 번째 항은 빼기
    if i % 2 == 1:
        total += 1 / i
    else:
        total -= 1 / i

    # 각 항까지의 누적 합 출력
    print(f"{i}항까지의 합: {total:.4f}")

    i += 1
