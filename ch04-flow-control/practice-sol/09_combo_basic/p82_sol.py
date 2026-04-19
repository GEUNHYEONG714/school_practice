"""
실습 82 풀이: ROT13 암호화
"""

s = input("문자열을 입력하세요: ")
result = ""

for ch in s:
    if ch.isupper():
        # 대문자: 13칸 밀고 26으로 순환
        code = ord(ch) - ord("A")
        code = (code + 13) % 26
        result += chr(code + ord("A"))
    elif ch.islower():
        # 소문자: 13칸 밀고 26으로 순환
        code = ord(ch) - ord("a")
        code = (code + 13) % 26
        result += chr(code + ord("a"))
    else:
        # 알파벳이 아닌 문자는 그대로
        result += ch

print(result)
