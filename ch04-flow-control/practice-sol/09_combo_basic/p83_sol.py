"""
실습 83 풀이: 소인수분해
"""

n = int(input("정수를 입력하세요: "))

result = ""
divisor = 2

# 2부터 시작하여 나누어떨어지면 계속 나누기
while n > 1:
    while n % divisor == 0:
        if result != "":
            result += " x "
        result += str(divisor)
        n = n // divisor
    divisor += 1

print(result)
