"""
실습 14 풀이: 완전제곱수 찾기
"""

N = int(input("N을 입력하세요: "))

# 1부터 제곱값이 N 이하인 동안 반복
i = 1
while i * i <= N:
    print(i * i)
    i += 1
