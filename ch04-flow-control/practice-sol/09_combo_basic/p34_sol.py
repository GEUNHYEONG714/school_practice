"""
실습 34 풀이: 모음 세기
"""

text = input("문자열을 입력하세요: ")
vowel_count = 0

# 한 글자씩 확인하면서 모음이면 카운트
for char in text:
    # 대소문자 구분 없이 비교하기 위해 소문자로 변환
    if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() == "u":
        vowel_count += 1

print("모음 개수:", vowel_count)
