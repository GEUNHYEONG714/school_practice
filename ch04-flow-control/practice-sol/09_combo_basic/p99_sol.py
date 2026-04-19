"""
실습 99 풀이: 가위바위보 N판
"""

n = int(input("판 수: "))

win = 0
lose = 0
draw = 0

for i in range(1, n + 1):
    player = input()

    # 컴퓨터 패턴: 1판=바위, 2판=보, 3판=가위, 4판=바위, ...
    r = i % 3
    if r == 1:
        computer = "바위"
    elif r == 2:
        computer = "보"
    else:
        computer = "가위"

    # 승패 판정
    if player == computer:
        result = "무"
        draw += 1
    elif (player == "가위" and computer == "보") or \
         (player == "바위" and computer == "가위") or \
         (player == "보" and computer == "바위"):
        result = "승"
        win += 1
    else:
        result = "패"
        lose += 1

    print(str(i) + "판: 플레이어(" + player + ") vs 컴퓨터(" + computer + ") -> " + result)

print("전적: " + str(win) + "승 " + str(lose) + "패 " + str(draw) + "무")
