"""
실습 67 풀이: 배수 판별기
"""

num = int(input("숫자를 입력하세요: "))
n = int(input("N을 입력하세요: "))

# 2부터 N까지 각각의 배수인지 판별
for i in range(2, n + 1):
    if num % i == 0:
        print(str(i) + "의 배수입니다.")
    else:
        print(str(i) + "의 배수가 아닙니다.")
