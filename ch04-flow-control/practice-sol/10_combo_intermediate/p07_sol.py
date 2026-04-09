"""
실습 7 풀이: 최소공배수
"""

a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))

# 원래 값 저장 (LCM 계산에 사용)
original_a = a
original_b = b

# 1단계: 유클리드 호제법으로 최대공약수 구하기
temp_a = a
temp_b = b

while temp_b != 0:
    remainder = temp_a % temp_b
    temp_a = temp_b
    temp_b = remainder

gcd = temp_a  # temp_b가 0이 되면 temp_a가 GCD

# 2단계: LCM = a * b // GCD
lcm = original_a * original_b // gcd

print("최대공약수(GCD):", gcd)
print("최소공배수(LCM):", lcm)
