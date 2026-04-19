"""
실습 75 풀이: 문자 종류 카운트
"""

s = input("문자열을 입력하세요: ")
upper = 0
lower = 0
digit = 0
other = 0

# 문자열을 순회하며 종류별로 카운트
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        other += 1

print("대문자:", upper)
print("소문자:", lower)
print("숫자:", digit)
print("기타:", other)
