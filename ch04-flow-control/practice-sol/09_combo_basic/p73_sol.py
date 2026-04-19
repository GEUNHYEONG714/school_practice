"""
실습 73 풀이: 이메일 유효성 검사
"""

s = input("문자열을 입력하세요: ")

# 플래그 변수 초기화
has_at = False
has_dot = False

# 문자열을 순회하며 '@'와 '.'의 존재 여부 확인
for ch in s:
    if ch == "@":
        has_at = True
    elif ch == ".":
        has_dot = True

# 둘 다 있으면 유효, 아니면 무효
if has_at and has_dot:
    print("유효")
else:
    print("무효")
