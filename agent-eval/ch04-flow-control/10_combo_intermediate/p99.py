"""
TITLE: 암호 해독 (치환)
DIFFICULTY: hard
TAGS: cipher, substitution, string, loop, if
EVAL: stdio

DESCRIPTION:
첫 줄에 암호문(대문자와 공백으로 구성)을 입력받습니다.
둘째 줄에 치환 키를 입력받습니다: 26개 대문자가 공백 없이 나열된 문자열.
키의 i번째 문자는 알파벳 i번째 글자(A=0, B=1, ...)가 암호화된 결과입니다.
즉, 원문의 A가 키[0]으로 암호화되었으므로, 암호문에서 키[0]을 찾으면 원문 A입니다.
복호화하여 원문을 출력하세요. 공백은 그대로 유지합니다.
(리스트/딕셔너리/함수 사용 금지, 변수만 사용)

예시:
- 키: "BCDEFGHIJKLMNOPQRSTUVWXYZA" (각 글자를 +1 시프트)
- 암호문: "IFMMP" → 각 글자를 키에서 찾아 위치(원문) 복원 → "HELLO"
"""
# META_TESTS:
# - stdin: "IFMMP\nBCDEFGHIJKLMNOPQRSTUVWXYZA"
#   expected_stdout: "HELLO"
# - stdin: "XYZ\nBCDEFGHIJKLMNOPQRSTUVWXYZA"
#   expected_stdout: "WXY"
# - stdin: "B D\nBCDEFGHIJKLMNOPQRSTUVWXYZA"
#   expected_stdout: "A C"

# 암호 해독: 치환 암호를 복호화하세요.
cipher = input()
key = input()
# TODO
