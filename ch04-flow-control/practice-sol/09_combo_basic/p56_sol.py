"""
실습 56 풀이: 주사위 합 판정
"""

d1 = int(input("첫 번째 주사위: "))
d2 = int(input("두 번째 주사위: "))

print("주사위: " + str(d1) + ", " + str(d2))

# 합이 7인지 먼저 확인, 그 다음 더블 확인
if d1 + d2 == 7:
    print("럭키세븐!")
elif d1 == d2:
    print("더블!")
else:
    print("합: " + str(d1 + d2))
