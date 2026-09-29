"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 42: 암호 만들기

문자열을 입력받아 각 글자를 알파벳 순서에서 다음 글자로 변환하세요.
a → b, b → c, ..., z → a

힌트: ord("a")는 글자의 숫자 코드를 반환합니다. (a=97, b=98, ...)
      chr(숫자)는 숫자를 글자로 변환합니다.
      알파벳이 아닌 문자(공백 등)는 그대로 출력합니다.
"""

text = input("문자열을 입력하세요: ")
result = ""

# 아래에 각 글자를 다음 알파벳으로 변환하는 코드를 작성하세요

# 문자열 대입
for str in text:
    # 소문자인 경우
    if "a" <= str <= "z":
        print((ord(str) - ord("a") + 1) % 26)  
        result += chr((ord(str) - ord("a") + 1) % 26 + ord("a"))
    # 대문자인 경우
    elif "A" <= str <= "Z":
        result += chr((ord(str) - ord("A") + 1) % 26 + ord("A"))
    # 영어가 아닌 경우
    else:
        result += str

# 출력
print("암호:", result)

"""
[실행 결과 예시] (입력: hello)
문자열을 입력하세요: hello
암호: ifmmp

[실행 결과 예시 2] (입력: xyz)
문자열을 입력하세요: xyz
암호: yza
"""
