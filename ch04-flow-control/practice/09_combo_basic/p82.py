"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 82: ROT13 암호화

문자열을 입력받아 ROT13 암호화를 적용하여 출력하시오.

ROT13 규칙:
- 알파벳을 13칸 뒤로 밀어 변환 (a→n, b→o, ..., n→a, z→m)
- 대문자와 소문자 모두 각각 변환하되 대소문자를 유지
- 알파벳이 아닌 문자는 그대로 유지

힌트: ord()와 chr()을 사용하여 문자 코드를 계산합니다.
      알파벳 범위를 넘어가면 26을 빼서 순환시킵니다.
"""

s = input("문자열을 입력하세요: ")
result = ""
# 아래에 코드를 작성하세요

# ROT13 암호화
for i in s:
    # 소문자 처리
    if "a" <= i <= "z":
        num = ord(i) + 13

        # 범위 초과 시 순환
        if num > ord("z"):
            num -= 26

        result += chr(num)

    # 대문자 처리
    elif "A" <= i <= "Z":
        num = ord(i) + 13

        # 범위 초과 시 순환
        if num > ord("Z"):
            num -= 26

        result += chr(num)

    # 나머지 문자 유지
    else:
        result += i

# 출력
print(result)
"""
[실행 결과 예시] (입력: Hello)
Uryyb

[실행 결과 예시] (입력: abc)
nop
"""
