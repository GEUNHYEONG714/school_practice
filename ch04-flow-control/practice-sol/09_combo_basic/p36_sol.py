"""
실습 36 풀이: 문자열 뒤집기
"""

text = input("문자열을 입력하세요: ")
result = ""

# 마지막 인덱스부터 0까지 역순으로 반복
for i in range(len(text) - 1, -1, -1):
    result += text[i]

print("뒤집은 문자열:", result)
