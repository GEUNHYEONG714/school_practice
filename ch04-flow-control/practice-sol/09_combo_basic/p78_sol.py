"""
실습 78 풀이: 모음 제거
"""

s = input("문장을 입력하세요: ")
result = ""

# 모음 목록
vowels = "aeiouAEIOU"

# 모음이 아닌 문자만 결과에 추가
for ch in s:
    if ch not in vowels:
        result += ch

print(result)
