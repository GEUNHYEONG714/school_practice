"""
실습 6 풀이: 요일 판별
"""

day = int(input("숫자를 입력하세요 (1~7): "))

# 1~7 각각에 대응하는 요일을 elif로 연결
if day == 1:
    name = "월요일"
elif day == 2:
    name = "화요일"
elif day == 3:
    name = "수요일"
elif day == 4:
    name = "목요일"
elif day == 5:
    name = "금요일"
elif day == 6:
    name = "토요일"
elif day == 7:
    name = "일요일"
else:
    name = ""

# 유효한 입력이면 요일 출력, 아니면 오류 메시지
if name != "":
    print(str(day) + " → " + name)
else:
    print("잘못된 입력입니다.")
