"""
실습 36 풀이: 타이머 (카운트다운)
"""

minutes = int(input("타이머 시간(분): "))
seconds = 0  # 초는 0부터 시작

# 카운트다운
while True:
    # 현재 시간 출력 (초를 두 자리로 표시)
    if seconds < 10:
        sec_str = "0" + str(seconds)
    else:
        sec_str = str(seconds)
    print(str(minutes) + "분 " + sec_str + "초")

    # 0분 0초이면 종료
    if minutes == 0 and seconds == 0:
        print("타이머 종료!")
        break

    # 1초 감소
    seconds = seconds - 1

    # 초가 음수가 되면 분을 줄이고 초를 59로
    if seconds < 0:
        minutes = minutes - 1
        seconds = 59
