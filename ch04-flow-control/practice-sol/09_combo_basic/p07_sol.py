"""
실습 7 풀이: 체질량(BMI) 판정
"""

height = float(input("키를 입력하세요 (cm): "))
weight = float(input("몸무게를 입력하세요 (kg): "))
age = int(input("나이를 입력하세요: "))

# BMI 계산 (키를 m로 변환)
height_m = height / 100
bmi = weight / (height_m ** 2)
print("BMI:", round(bmi, 2))

# 나이에 따라 다른 기준 적용
if age >= 20:
    # 성인 기준
    if bmi < 18.5:
        print("판정: 저체중")
    elif bmi < 23:
        print("판정: 정상")
    elif bmi < 25:
        print("판정: 과체중")
    else:
        print("판정: 비만")
else:
    # 청소년 기준
    if bmi < 17:
        print("판정: 저체중 (청소년 기준)")
    elif bmi < 23:
        print("판정: 정상 (청소년 기준)")
    else:
        print("판정: 과체중 주의 (청소년 기준)")
