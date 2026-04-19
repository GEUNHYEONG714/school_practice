"""
실습 85 풀이: 이진수 1의 개수
"""

n = int(input("정수를 입력하세요: "))

# 2로 나눈 나머지가 1이면 카운트 증가
count = 0

while n > 0:
    if n % 2 == 1:
        count += 1
    n = n // 2

print(count)
