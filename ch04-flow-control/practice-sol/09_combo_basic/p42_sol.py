"""
실습 42 풀이: 암호 만들기
"""

text = input("문자열을 입력하세요: ")
result = ""

for char in text:
    if "a" <= char <= "z":
        # 소문자: 다음 알파벳으로 변환 (z → a 순환)
        if char == "z":
            result += "a"
        else:
            result += chr(ord(char) + 1)
    elif "A" <= char <= "Z":
        # 대문자: 다음 알파벳으로 변환 (Z → A 순환)
        if char == "Z":
            result += "A"
        else:
            result += chr(ord(char) + 1)
    else:
        # 알파벳이 아닌 문자는 그대로
        result += char

print("암호:", result)
