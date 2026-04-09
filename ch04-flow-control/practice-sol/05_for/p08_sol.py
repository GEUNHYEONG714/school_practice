"""
실습 8 풀이: 팩토리얼 계산
"""

n = int(input("숫자를 입력하세요: "))

# 곱셈 누적 변수는 1부터 시작 (0이면 결과가 항상 0이 된다)
result = 1

# 1부터 n까지 차례로 곱한다
for i in range(1, n + 1):
    result *= i  # result = result * i

print(str(n) + "! =", result)
