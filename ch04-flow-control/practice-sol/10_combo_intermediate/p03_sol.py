"""
실습 3 풀이: 완전수 찾기
"""

n = int(input("N을 입력하세요: "))

# 2부터 N까지 각 숫자를 검사 (1은 완전수가 아님)
for num in range(2, n + 1):
    divisor_sum = 0  # 약수의 합
    divisors = ""    # 약수 출력용 문자열

    # 1부터 num//2까지 약수인지 확인
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisor_sum += i
            # 약수 문자열 만들기
            if divisors == "":
                divisors = str(i)
            else:
                divisors = divisors + " + " + str(i)

    # 약수의 합이 자기 자신과 같으면 완전수
    if divisor_sum == num:
        print(str(num) + " = " + divisors)
