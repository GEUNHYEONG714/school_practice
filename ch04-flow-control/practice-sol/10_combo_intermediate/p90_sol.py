"""
실습 90 풀이: 전광판 문자
"""
ch = input()

# 소문자 → 대문자 변환
if ch == "a":
    ch = "A"
elif ch == "b":
    ch = "B"
elif ch == "c":
    ch = "C"

if ch == "A":
    print(" *** ")
    print("*   *")
    print("*****")
    print("*   *")
    print("*   *")
elif ch == "B":
    print("**** ")
    print("*   *")
    print("**** ")
    print("*   *")
    print("**** ")
elif ch == "C":
    print(" ****")
    print("*    ")
    print("*    ")
    print("*    ")
    print(" ****")
else:
    print("지원하지 않는 문자입니다.")
