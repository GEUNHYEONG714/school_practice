"""
실습 3 풀이: 교통수단 추천
"""

distance = float(input("거리를 입력하세요 (km): "))

# 거리가 짧은 순서대로 비교한다
if distance < 2:
    transport = "도보"
elif distance < 5:
    transport = "자전거"
elif distance < 20:
    transport = "버스"
else:
    transport = "지하철"

print("거리: " + str(distance) + "km")
print("추천 교통수단: " + transport)
