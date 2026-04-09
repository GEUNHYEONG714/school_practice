"""
실습 38 풀이: 단어 마스킹
"""

text = input("문자열을 입력하세요: ")
result = ""

# 인덱스로 접근하여 첫/마지막만 원래 글자, 나머지는 *
for i in range(len(text)):
    if i == 0 or i == len(text) - 1:
        result += text[i]  # 첫 글자와 마지막 글자는 그대로
    else:
        result += "*"  # 나머지는 * 처리

print("마스킹 결과:", result)
