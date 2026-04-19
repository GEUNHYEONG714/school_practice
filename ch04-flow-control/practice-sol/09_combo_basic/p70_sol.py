"""
실습 70 풀이: 숫자 분해
"""

num = int(input("3자리 정수를 입력하세요: "))

# 각 자리수 분리
h = num // 100
t = (num % 100) // 10
o = num % 10

print("백의자리: " + str(h))
print("십의자리: " + str(t))
print("일의자리: " + str(o))
print("합: " + str(h + t + o))
print("곱: " + str(h * t * o))
