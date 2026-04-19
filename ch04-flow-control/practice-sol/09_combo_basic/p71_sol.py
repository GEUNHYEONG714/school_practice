"""
실습 71 풀이: 연속 같은 문자
"""

s = input("문자열을 입력하세요: ")

max_count = 1
current_count = 1

# 두 번째 문자부터 이전 문자와 비교
i = 1
while i < len(s):
    if s[i] == s[i - 1]:
        current_count += 1
    else:
        current_count = 1

    # 최대값 갱신
    if current_count > max_count:
        max_count = current_count

    i += 1

print(max_count)
