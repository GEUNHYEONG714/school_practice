"""
TITLE: 암호 해독 (치환)
DIFFICULTY: hard
TAGS: cipher, substitution, string, loop, if
EVAL: stdio

DESCRIPTION:
치환 암호를 복호화(decode)하는 문제입니다.

입력:
- 첫 줄: 암호문 (대문자 A~Z와 공백으로만 구성)
- 둘째 줄: 26글자 치환 키 (A~Z가 공백 없이 나열된 문자열)

키 해석 (암호화 관점):
- 키의 i번째 문자는 "원문의 i번째 알파벳(A=0, B=1, ..., Z=25)이 암호화된 결과"입니다.
- 예: 키[0]='B' 이면 원문 'A' → 암호문 'B'로 암호화된 것입니다.
- 예: 키[1]='C' 이면 원문 'B' → 암호문 'C'로 암호화된 것입니다.

복호화 방법 (decode):
- 암호문의 각 글자 c에 대해, 키에서 c가 몇 번째 위치(index j)에 있는지 찾습니다.
- 그 j번째 알파벳(chr(65+j))이 원문 글자입니다.
- 즉, 암호문 'B'가 키[0]에 있으므로 원문은 'A'로 되돌려집니다.
- 공백 문자는 복호화하지 않고 그대로 유지합니다.

예시:
- 키: "BCDEFGHIJKLMNOPQRSTUVWXYZA" (각 알파벳을 +1 시프트하여 암호화한 키)
  - 원문 'A' → 암호문 'B' (키[0]='B'), 원문 'H' → 암호문 'I' (키[7]='I')
- 암호문: "IFMMP"
  - 'I'는 키[7]에 있음 → 원문 'H'
  - 'F'는 키[4]에 있음 → 원문 'E'
  - 'M'은 키[11]에 있음 → 원문 'L'
  - 'M' → 'L'
  - 'P'는 키[14]에 있음 → 원문 'O'
  - 결과: "HELLO"
"""
# META_TESTS:
# - stdin: "IFMMP\nBCDEFGHIJKLMNOPQRSTUVWXYZA"
#   expected_stdout: "HELLO"
# - stdin: "XYZ\nBCDEFGHIJKLMNOPQRSTUVWXYZA"
#   expected_stdout: "WXY"
# - stdin: "B D\nBCDEFGHIJKLMNOPQRSTUVWXYZA"
#   expected_stdout: "A C"

# 암호 해독: 치환 암호를 복호화하세요.
# 암호문의 각 글자 c를 키에서 찾아 그 위치(index)에 해당하는 알파벳이 원문.
cipher = input()
key = input()
# TODO
