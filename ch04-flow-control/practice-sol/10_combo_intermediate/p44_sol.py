"""
실습 44 풀이: 암호 해독 (시저 암호)
"""

mode = int(input("모드 선택 (1:인코딩, 2:디코딩): "))
shift = int(input("이동 칸수(N)를 입력하세요: "))
text = input("문장을 입력하세요: ")

# 디코딩이면 반대 방향으로 이동
if mode == 2:
    shift = -shift

result = ""
i = 0

# 문장의 각 글자를 순회
while i < len(text):
    ch = text[i]
    code = ord(ch)

    # 소문자 처리
    if ord('a') <= code <= ord('z'):
        # a를 기준으로 이동 후 26으로 순환
        new_code = (code - ord('a') + shift) % 26 + ord('a')
        result = result + chr(new_code)
    # 대문자 처리
    elif ord('A') <= code <= ord('Z'):
        new_code = (code - ord('A') + shift) % 26 + ord('A')
        result = result + chr(new_code)
    # 알파벳이 아닌 문자는 그대로
    else:
        result = result + ch

    i += 1

print("결과:", result)
