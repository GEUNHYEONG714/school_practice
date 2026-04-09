"""
실습 37 풀이: 특정 문자 제거
"""

text = input("문자열을 입력하세요: ")
remove = input("제거할 문자를 입력하세요: ")
result = ""

# 제거할 문자가 아닌 경우에만 결과에 추가
for char in text:
    if char != remove:
        result += char

print("결과:", result)
