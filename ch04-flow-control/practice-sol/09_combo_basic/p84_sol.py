"""
실습 84 풀이: 진법 변환 (10진법 → 8진법)
"""

n = int(input("정수를 입력하세요: "))

# 8로 나눈 나머지를 문자열 앞에 추가
result = ""

while n > 0:
    remainder = n % 8
    result = str(remainder) + result
    n = n // 8

print(result)
