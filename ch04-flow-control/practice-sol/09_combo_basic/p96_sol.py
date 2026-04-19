"""
실습 96 풀이: 도형 넓이 계산기
"""

shape = input("도형(원/삼각형/사각형): ")

if shape == "원":
    r = int(input("반지름: "))
    area = r * r * 3.14
    print("넓이:", format(area, ".2f"))
elif shape == "삼각형":
    base = int(input("밑변: "))
    height = int(input("높이: "))
    area = base * height / 2
    print("넓이:", format(area, ".1f"))
elif shape == "사각형":
    width = int(input("가로: "))
    height = int(input("세로: "))
    area = width * height
    print("넓이:", area)
