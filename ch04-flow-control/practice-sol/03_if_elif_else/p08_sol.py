"""
실습 8 풀이: 온도별 옷차림 추천
"""

temp = float(input("현재 기온을 입력하세요 (°C): "))

# 낮은 온도부터 비교하여 추천 옷차림 결정
if temp < 5:
    clothes = "패딩, 두꺼운 목도리"
elif temp < 10:
    clothes = "코트, 니트"
elif temp < 20:
    clothes = "자켓, 가디건"
elif temp < 28:
    clothes = "반팔, 얇은 셔츠"
else:
    clothes = "민소매, 반바지"

print("현재 기온: " + str(temp) + "°C")
print("추천 옷차림: " + clothes)
