"""
실습 20 풀이: 연속된 수의 합으로 표현하기
"""

N = int(input("N을 입력하세요: "))

# 시작 수를 1부터 N//2까지 시도 (2개 이상의 연속 수)
start = 1
while start <= N // 2:
    # start부터 연속된 수를 더해가며 N을 만들 수 있는지 확인
    total = 0
    current = start

    while total < N:
        total += current
        current += 1

    # 합이 정확히 N이고, 2개 이상의 수를 사용한 경우
    if total == N and current - start >= 2:
        # 출력 형식 만들기: N = a + b + c + ...
        result = str(N) + " = "
        k = start
        while k < current:
            if k > start:
                result += " + "
            result += str(k)
            k += 1
        print(result)

    start += 1
