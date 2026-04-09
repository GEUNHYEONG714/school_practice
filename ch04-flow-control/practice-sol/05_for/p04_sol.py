"""
실습 4 풀이: 1부터 N까지의 합 구하기
"""

n = int(input("숫자를 입력하세요: "))

# 합계를 저장할 변수 (0부터 시작)
total = 0

# range(1, n+1): 1부터 n까지 반복
for i in range(1, n + 1):
    total += i  # 현재 숫자를 합계에 더한다

print("1부터", n, "까지의 합:", total)
