"""
실습 77 풀이: 두 문자열 교차 출력
"""

s1 = input("첫 번째 문자열: ")
s2 = input("두 번째 문자열: ")
result = ""

# 두 문자열 중 긴 길이만큼 반복
longer = len(s1)
if len(s2) > longer:
    longer = len(s2)

for i in range(longer):
    # s1의 i번째 문자가 있으면 추가
    if i < len(s1):
        result += s1[i]
    # s2의 i번째 문자가 있으면 추가
    if i < len(s2):
        result += s2[i]

print(result)
