"""
실습 74 풀이: 단어 첫 글자 대문자 변환
"""

s = input("문장을 입력하세요: ")
result = ""

# 첫 글자도 대문자로 변환해야 하므로 플래그를 True로 시작
capitalize_next = True

for ch in s:
    if ch == " ":
        result += ch
        # 공백 다음 글자를 대문자로 변환하도록 플래그 설정
        capitalize_next = True
    else:
        if capitalize_next:
            result += ch.upper()
            capitalize_next = False
        else:
            result += ch

print(result)
