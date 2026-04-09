"""
실습 35 풀이: 대문자 변환 출력
"""

text = input("문자열을 입력하세요: ")

# 한 글자씩 대문자로 변환하여 출력
for char in text:
    print(char.upper(), end="")

print()  # 마지막 줄바꿈
