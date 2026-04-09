"""
실습 5 풀이: 숫자 뒤집기
"""

num = int(input("양의 정수를 입력하세요: "))

reverse = 0

# num이 0보다 큰 동안 반복
while num > 0:
    digit = num % 10     # 마지막 자리 숫자 꺼내기
    reverse = reverse * 10 + digit  # 뒤집은 숫자에 추가
    num //= 10           # 마지막 자리 제거

print(f"뒤집은 숫자: {reverse}")
