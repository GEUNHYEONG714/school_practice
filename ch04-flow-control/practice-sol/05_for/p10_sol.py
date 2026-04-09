"""
실습 10 풀이: 누적 곱 계산
"""

count = int(input("숫자의 개수를 입력하세요: "))

# 곱셈 누적 변수는 1부터 시작
result = 1

# count번 반복하며 숫자를 입력받는다
for i in range(1, count + 1):
    num = int(input(str(i) + "번째 숫자를 입력하세요: "))
    result *= num  # 입력받은 숫자를 누적 곱한다

print("누적 곱:", result)
