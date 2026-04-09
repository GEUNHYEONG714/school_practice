"""
실습 39 풀이: 온도 조절기
"""

current_temp = int(input("현재 온도: "))
target_temp = int(input("목표 온도: "))

if current_temp == target_temp:
    # 이미 목표 온도인 경우
    print("이미 목표 온도입니다.")

elif current_temp < target_temp:
    # 난방 모드 (온도 올리기)
    print("난방 모드를 시작합니다.")
    while current_temp < target_temp:
        next_temp = current_temp + 1
        print("현재 온도: " + str(current_temp) + "도 → " + str(next_temp) + "도")
        current_temp = next_temp
    print("목표 온도 " + str(target_temp) + "도에 도달했습니다!")

else:
    # 냉방 모드 (온도 내리기)
    print("냉방 모드를 시작합니다.")
    while current_temp > target_temp:
        next_temp = current_temp - 1
        print("현재 온도: " + str(current_temp) + "도 → " + str(next_temp) + "도")
        current_temp = next_temp
    print("목표 온도 " + str(target_temp) + "도에 도달했습니다!")
