"""
실습 81 풀이: 단어 뒤집기 (문장)
"""

s = input("문장을 입력하세요: ")
result = ""
word = ""

# 문자열을 순회하며 단어 단위로 뒤집기
for ch in s:
    if ch == " ":
        # 공백을 만나면 모은 단어를 뒤집어서 결과에 추가
        result += word[::-1] + " "
        word = ""
    else:
        word += ch

# 마지막 단어 처리
result += word[::-1]

print(result)
