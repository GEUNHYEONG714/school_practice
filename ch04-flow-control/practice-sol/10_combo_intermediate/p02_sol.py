"""
실습 2 풀이: 1~N 소수 출력
"""

n = int(input("N을 입력하세요: "))

count = 0  # 소수 개수

# 2부터 N까지 각 숫자를 검사
for num in range(2, n + 1):
    # 소수 여부 판별
    is_prime = True

    # 2부터 제곱근까지 약수가 있는지 확인
    j = 2
    while j * j <= num:
        if num % j == 0:
            is_prime = False
            break
        j += 1

    # 소수이면 출력
    if is_prime:
        print(num, end=" ")
        count += 1

print()  # 줄바꿈
print("소수 개수:", count)
