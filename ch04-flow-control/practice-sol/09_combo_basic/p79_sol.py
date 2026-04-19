"""
실습 79 풀이: 카멜케이스 변환
"""

s = input("문자열을 입력하세요: ")
result = ""

# '_' 다음 문자를 대문자로 변환하기 위한 플래그
capitalize_next = False

for ch in s:
    if ch == "_":
        # 언더스코어를 만나면 플래그 설정
        capitalize_next = True
    else:
        if capitalize_next:
            result += ch.upper()
            capitalize_next = False
        else:
            result += ch

print(result)
