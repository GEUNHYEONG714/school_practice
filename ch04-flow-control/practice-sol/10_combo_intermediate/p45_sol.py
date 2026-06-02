"""
실습 45 풀이: 미로 탈출 (1차원)
"""

pos = 0       # 현재 위치
score = 0     # 점수
moves = 0     # 이동 횟수

# 함정/보물 위치
trap1 = 3     # 함정 → 위치 0으로
trap2 = 7     # 함정 → 위치 4로
treasure = 5  # 보물 → 점수 +10
exit_pos = 9  # 탈출구

# 트리거 가능 여부 (1=발동 가능, 0=이미 발동되어 통과만)
trap1_active = 1
trap2_active = 1
got_treasure = 0

print("=== 1차원 미로 탈출 ===")
print("탈출구는 위치 9입니다. 함정을 피하고 보물을 찾으세요!")
print("현재 위치:", pos)

while pos != exit_pos:
    direction = int(input("좌(1)/우(2) 입력: "))

    # 이동 처리
    if direction == 1:
        new_pos = pos - 1
    elif direction == 2:
        new_pos = pos + 1
    else:
        print("1 또는 2를 입력하세요.")
        continue

    # 범위 확인
    if new_pos < 0 or new_pos > 9:
        print("이동할 수 없습니다! (범위 초과)")
        continue

    pos = new_pos
    moves += 1

    # 함정/보물/탈출구 확인 (각 트리거는 첫 진입 시 한 번만)
    if pos == trap1 and trap1_active == 1:
        print("함정! 위치 0으로 되돌아갑니다!")
        pos = 0
        trap1_active = 0
    elif pos == trap2 and trap2_active == 1:
        print("함정! 위치 4로 되돌아갑니다!")
        pos = 4
        trap2_active = 0
    elif pos == treasure and got_treasure == 0:
        print("보물 발견! 점수 +10!")
        score += 10
        got_treasure = 1
    elif pos == exit_pos:
        print("탈출구에 도달했습니다!")

    print("현재 위치:", pos)

print("탈출 성공! 총 이동 횟수: " + str(moves) + ", 점수: " + str(score))
