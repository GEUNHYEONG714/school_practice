"""
실습 6 풀이: BMI 판정
"""

height = float(input("키를 입력하세요 (cm): "))
weight = float(input("몸무게를 입력하세요 (kg): "))

# cm를 m로 변환한 뒤 BMI 계산
height_m = height / 100
bmi = weight / (height_m ** 2)

# BMI 구간별 판정
if bmi < 18.5:
    result = "저체중"
elif bmi < 23:
    result = "정상"
elif bmi < 25:
    result = "과체중"
else:
    result = "비만"

print("키: " + str(height) + "cm, 몸무게: " + str(weight) + "kg")
print("BMI: " + str(round(bmi, 2)))
print("판정: " + result)
