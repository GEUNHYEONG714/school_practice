"""
실습 41 풀이: 패턴 반복 출력
"""

text = input("문자열을 입력하세요: ")
n = int(input("반복 횟수를 입력하세요: "))

# 각 글자를 n번씩 반복 출력
for char in text:
    for j in range(n):
        print(char, end="")

print()  # 마지막 줄바꿈
