"""
실습 9 풀이: 간단한 계산기
"""

num1 = float(input("첫 번째 수를 입력하세요: "))
op = input("연산자를 입력하세요 (+, -, *, /): ")
num2 = float(input("두 번째 수를 입력하세요: "))

# 연산자에 따라 계산 수행
if op == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif op == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif op == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif op == "/":
    # 0으로 나누기 방지
    if num2 == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
else:
    # 지원하지 않는 연산자
    print("지원하지 않는 연산자입니다.")
