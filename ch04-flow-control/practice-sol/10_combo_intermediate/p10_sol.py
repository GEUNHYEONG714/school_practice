"""
실습 10 풀이: 카프리카 수 (Kaprekar Number)
"""

n = int(input("N을 입력하세요: "))

print("카프리카 수:")

for num in range(1, n + 1):
    squared = num * num  # 제곱 계산

    # 1은 특수 케이스로 카프리카 수에 포함
    if num == 1:
        print(1)
        continue

    # 제곱한 수의 자릿수 구하기
    digits = 0
    temp = squared
    while temp > 0:
        digits += 1
        temp //= 10

    # 오른쪽 부분의 자릿수를 1부터 digits-1까지 시도
    # (오른쪽 부분이 전체 자릿수이면 왼쪽이 0이므로 제외)
    d = 1
    while d < digits:
        # 10^d로 나누어 왼쪽/오른쪽 분리
        divisor = 1
        for _ in range(d):
            divisor *= 10

        right = squared % divisor       # 오른쪽 부분
        left = squared // divisor       # 왼쪽 부분

        # 오른쪽 부분이 0이면 유효하지 않음 (건너뜀)
        if right != 0 and left + right == num:
            # 오른쪽 부분을 자릿수에 맞게 0-패딩하여 출력
            right_str = str(right)
            while len(right_str) < d:
                right_str = "0" + right_str

            print(str(num) + ": " + str(num) + "^2 = " + str(squared) + ", " + str(left) + " + " + right_str + " = " + str(num))
            break

        d += 1
