"""
실습 92 풀이: 행맨 게임
"""
# 정답: PYTHON (6글자)
# 각 글자가 공개되었는지 플래그
found_P = 0
found_Y = 0
found_T = 0
found_H = 0
found_O = 0
found_N = 0

for i in range(5):
    guess = input()

    # 맞춘 글자 업데이트
    if guess == "P":
        found_P = 1
    if guess == "Y":
        found_Y = 1
    if guess == "T":
        found_T = 1
    if guess == "H":
        found_H = 1
    if guess == "O":
        found_O = 1
    if guess == "N":
        found_N = 1

    # 현재 상태 출력
    c1 = "_"
    c2 = "_"
    c3 = "_"
    c4 = "_"
    c5 = "_"
    c6 = "_"
    if found_P == 1:
        c1 = "P"
    if found_Y == 1:
        c2 = "Y"
    if found_T == 1:
        c3 = "T"
    if found_H == 1:
        c4 = "H"
    if found_O == 1:
        c5 = "O"
    if found_N == 1:
        c6 = "N"

    print(c1 + " " + c2 + " " + c3 + " " + c4 + " " + c5 + " " + c6)

# 성공/실패 판정
if found_P == 1 and found_Y == 1 and found_T == 1 and found_H == 1 and found_O == 1 and found_N == 1:
    print("성공")
else:
    print("실패")
