"""
실습 65 풀이: 별 사각형
"""

width = int(input("가로를 입력하세요: "))
height = int(input("세로를 입력하세요: "))

# 세로만큼 반복하며 가로 길이의 별 출력
for i in range(height):
    print("*" * width)
