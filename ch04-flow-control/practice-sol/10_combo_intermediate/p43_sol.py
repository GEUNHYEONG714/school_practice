"""
실습 43 풀이: 가위바위보 5판 3선승
"""

# 컴퓨터 패턴 (1:가위, 2:바위, 3:보)
com_r1 = 1  # 1라운드: 가위
com_r2 = 2  # 2라운드: 바위
com_r3 = 3  # 3라운드: 보
com_r4 = 1  # 4라운드: 가위
com_r5 = 2  # 5라운드: 바위

player_wins = 0
com_wins = 0
round_num = 1

print("=== 가위바위보 5판 3선승 ===")

while round_num <= 5 and player_wins < 3 and com_wins < 3:
    print()
    print("[라운드 " + str(round_num) + "]")
    player = int(input("가위(1)/바위(2)/보(3) 입력: "))

    # 라운드별 컴퓨터 선택 결정
    if round_num == 1:
        com = com_r1
    elif round_num == 2:
        com = com_r2
    elif round_num == 3:
        com = com_r3
    elif round_num == 4:
        com = com_r4
    else:
        com = com_r5

    # 이름 변환 (출력용)
    if player == 1:
        p_name = "가위"
    elif player == 2:
        p_name = "바위"
    else:
        p_name = "보"

    if com == 1:
        c_name = "가위"
    elif com == 2:
        c_name = "바위"
    else:
        c_name = "보"

    # 승패 판정
    # 무승부
    if player == com:
        result = "무승부"
    # 플레이어 승리 조건: 가위>보, 바위>가위, 보>바위
    elif (player == 1 and com == 3) or (player == 2 and com == 1) or (player == 3 and com == 2):
        result = "승리!"
        player_wins += 1
    else:
        result = "패배..."
        com_wins += 1

    print("나: " + p_name + " vs 컴퓨터: " + c_name + " → " + result)
    print("(현재 스코어) 나 " + str(player_wins) + " : " + str(com_wins) + " 컴퓨터")

    round_num += 1

# 최종 결과
print()
if player_wins > com_wins:
    print("나의 승리! (" + str(player_wins) + ":" + str(com_wins) + ")")
elif com_wins > player_wins:
    print("컴퓨터의 승리! (" + str(player_wins) + ":" + str(com_wins) + ")")
else:
    print("무승부! (" + str(player_wins) + ":" + str(com_wins) + ")")
