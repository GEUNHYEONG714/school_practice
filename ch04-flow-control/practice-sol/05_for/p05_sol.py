"""
실습 5 풀이: 홀수만 출력
"""

n = int(input("숫자를 입력하세요: "))

# 1부터 n까지 반복
for i in range(1, n + 1):
    # 2로 나눈 나머지가 1이면 홀수
    if i % 2 == 1:
        print(i)
