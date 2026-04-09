"""
실습 39 풀이: 회문 판별
"""

text = input("문자열을 입력하세요: ")
reversed_text = ""

# 문자열을 역순으로 뒤집기
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

# 원본과 뒤집은 문자열 비교
if text == reversed_text:
    print(text + "은(는) 회문입니다!")
else:
    print(text + "은(는) 회문이 아닙니다.")
