"""
실습 15 풀이: 소수 판별
"""

num = int(input("2 이상의 정수를 입력하세요: "))

is_prime = True  # 소수라고 가정하고 시작

# 2부터 (num-1)까지 나누어 본다
for i in range(2, num):
    if num % i == 0:
        # 나누어 떨어지면 소수가 아니다
        print(str(num) + "은(는) 소수가 아닙니다 (" + str(num) + " = " + str(i) + " x " + str(num // i) + ")")
        is_prime = False
        break  # 더 확인할 필요 없이 즉시 종료

# 끝까지 나누어 떨어지지 않았다면 소수
if is_prime:
    print(str(num) + "은(는) 소수입니다")
