"""
실습 5: BMI 계산기

키(cm)와 몸무게(kg)를 입력받아 BMI를 계산하세요.

BMI 공식: 몸무게(kg) / 키(m)의 제곱
주의: 키는 cm로 입력받지만, 공식에서는 m 단위를 사용합니다.

힌트: cm → m 변환은 / 100, 제곱은 ** 2를 사용합니다.
"""

height = int(input("키(cm)를 입력하세요: "))
weight = int(input("몸무게(kg)를 입력하세요: "))

# 아래에 BMI를 계산하여 출력하세요

# 키 출력
print(f"키: {height}cm")

# 몸무게 출력
print(f"몸무게: {weight}kg")

# bmi 계산(몸무게(kg) / 키(m) ** 2) 후 출력
bmi = weight / ((height / 100) ** 2)
print(f"BMI: {bmi}")

"""
[실행 결과 예시] (입력: 175, 70)
키: 175cm
몸무게: 70kg
BMI: 22.857142857142858
"""
