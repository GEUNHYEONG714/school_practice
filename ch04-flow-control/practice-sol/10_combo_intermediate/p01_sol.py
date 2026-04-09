"""
실습 1 풀이: 소수 판별
"""

num = int(input("2 이상의 정수를 입력하세요: "))

# 소수 여부를 저장하는 변수 (일단 소수라고 가정)
is_prime = True

# 2보다 작으면 소수가 아님
if num < 2:
    is_prime = False
else:
    # 2부터 num-1까지 나누어 떨어지는지 확인
    # 효율화: 제곱근까지만 확인 (i*i <= num)
    i = 2
    while i * i <= num:
        if num % i == 0:
            # 나누어 떨어지면 소수가 아님
            is_prime = False
            break
        i += 1

# 결과 출력
if is_prime:
    print(str(num) + "은(는) 소수입니다.")
else:
    print(str(num) + "은(는) 소수가 아닙니다.")
