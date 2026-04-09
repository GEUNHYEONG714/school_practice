"""
실습 6 풀이: 최대공약수 (유클리드 호제법)
"""

a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))

# 원래 값 저장 (출력용)
original_a = a
original_b = b

print("GCD(" + str(a) + ", " + str(b) + ") 계산 과정:")

# 유클리드 호제법: b가 0이 될 때까지 반복
while b != 0:
    quotient = a // b   # 몫
    remainder = a % b   # 나머지

    # 계산 과정 출력
    print("  " + str(a) + " ÷ " + str(b) + " = " + str(quotient) + " ... 나머지 " + str(remainder))

    # a에 b를, b에 나머지를 대입
    a = b
    b = remainder

# 반복이 끝나면 a가 최대공약수
print("최대공약수:", a)
