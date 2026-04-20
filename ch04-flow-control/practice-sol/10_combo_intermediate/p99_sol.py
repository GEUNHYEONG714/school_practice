"""
실습 99 풀이: 암호 해독 (치환)

키 해석: 키[i] = 원문의 i번째 알파벳(A=0, B=1,...)이 암호화된 글자
복호화: 암호문의 각 글자 c를 키에서 찾은 위치 j → 원문 = chr(65+j)
"""
cipher = input()
key = input()

result = ""
i = 0
while i < len(cipher):
    ch = cipher[i]
    if ch == " ":
        result += " "
    else:
        # 암호문 글자 ch가 key의 몇 번째 위치에 있는지 찾기
        j = 0
        while j < 26:
            if key[j] == ch:
                # j번째 알파벳이 원문
                # A=65, j번째 알파벳은 chr(65+j)
                result += chr(65 + j)
                j = 26  # 루프 종료
            j += 1
    i += 1

print(result)
