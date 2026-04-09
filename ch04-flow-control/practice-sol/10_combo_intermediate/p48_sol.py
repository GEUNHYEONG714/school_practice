"""
실습 48 풀이: 계단 오르기
"""

goal = 10  # 목표 계단 수
pos = 0    # 현재 위치
step_count = 0  # 이동 횟수

print("=== 계단 오르기 ===")
print("목표:", goal, "칸")
print("1칸(1) 또는 2칸(2)을 선택하여 올라가세요!")
print()

while pos < goal:
    choice = int(input("1칸(1) / 2칸(2) 선택: "))

    # 유효한 입력만 처리
    if choice != 1 and choice != 2:
        print("1 또는 2를 입력하세요.")
        continue

    pos += choice
    step_count += 1

    # 목표를 넘으면 목표에 맞춤
    if pos > goal:
        pos = goal

    # 진행 바 생성
    bar = ""
    i = 0
    while i < goal:
        if i < pos:
            bar = bar + "#"
        else:
            bar = bar + "-"
        i += 1

    print("[" + bar + "] " + str(pos) + "/" + str(goal) + "칸 (" + str(step_count) + "번째 이동)")

print()
print("축하합니다! 총 " + str(step_count) + "번 만에 계단을 올랐습니다!")
