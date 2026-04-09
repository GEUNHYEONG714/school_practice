"""
실습 16 풀이: 자릿수가 같은 수 (Repdigit)
"""

N = int(input("N을 입력하세요: "))

# 1부터 N까지 각 수에 대해 판별
num = 1
while num <= N:
    temp = num
    # 일의 자리 숫자를 기준으로 설정
    first_digit = temp % 10
    is_repdigit = True

    # 모든 자릿수가 같은지 확인
    while temp > 0:
        digit = temp % 10
        if digit != first_digit:
            is_repdigit = False
            break
        temp //= 10

    # 모든 자릿수가 동일하면 출력
    if is_repdigit:
        print(num)

    num += 1
