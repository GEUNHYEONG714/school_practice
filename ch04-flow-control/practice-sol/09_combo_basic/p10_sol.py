"""
실습 10 풀이: 가위바위보 확장
"""

print("=== 가위바위보 게임 ===")
print("1: 가위, 2: 바위, 3: 보")
user = int(input("선택하세요 (1/2/3): "))

# 컴퓨터 선택 (고정값)
computer = 2

# 입력값 유효성 확인
if user < 1 or user > 3:
    print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")
else:
    # 숫자를 이름으로 변환하여 출력
    if user == 1:
        user_name = "가위"
    elif user == 2:
        user_name = "바위"
    else:
        user_name = "보"

    if computer == 1:
        com_name = "가위"
    elif computer == 2:
        com_name = "바위"
    else:
        com_name = "보"

    print("당신:", user_name, "/ 컴퓨터:", com_name)

    # 승패 판정
    if user == computer:
        # 같으면 무승부
        print("무승부입니다! 😐")
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        # 가위>보, 바위>가위, 보>바위
        print("축하합니다! 당신이 이겼습니다! 🎉")
    else:
        print("아쉽게도 졌습니다. 😢")
