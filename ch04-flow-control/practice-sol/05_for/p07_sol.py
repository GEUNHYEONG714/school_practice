"""
실습 7 풀이: 거꾸로 카운트
"""

n = int(input("시작 숫자를 입력하세요: "))

# range(n, 0, -1): n부터 1까지 1씩 줄어들며 반복 (0은 포함되지 않음)
for i in range(n, 0, -1):
    print(i)
