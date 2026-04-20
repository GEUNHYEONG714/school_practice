"""
실습 80 풀이: 괄호 짝 검사
"""

s = input("문자열을 입력하세요: ")

# 여는 괄호와 닫는 괄호 개수 카운터
open_count = 0
close_count = 0

for ch in s:
    if ch == "(":
        open_count += 1
    elif ch == ")":
        close_count += 1

# 개수가 같으면 올바름 (괄호가 하나도 없는 경우 0 == 0 이므로 "올바름"이 출력됨)
if open_count == close_count:
    print("올바름")
else:
    print("올바르지 않음")
