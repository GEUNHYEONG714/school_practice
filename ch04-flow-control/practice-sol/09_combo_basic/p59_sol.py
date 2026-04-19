"""
실습 59 풀이: 택배 요금
"""

weight = int(input("무게(kg)를 입력하세요: "))
dist = int(input("거리(km)를 입력하세요: "))

# 기본료
fee = 3000

# 무게 추가 요금
if weight <= 2:
    fee += 0
elif weight <= 10:
    fee += 1000
else:
    fee += 3000

# 거리 추가 요금
if dist <= 50:
    fee += 0
elif dist <= 100:
    fee += 1500
else:
    fee += 3000

print("무게: " + str(weight) + "kg | 거리: " + str(dist) + "km")
print("택배 요금: " + str(fee) + "원")
