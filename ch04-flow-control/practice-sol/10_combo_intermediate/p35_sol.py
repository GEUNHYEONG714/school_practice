"""
실습 35 풀이: 엘리베이터 시뮬레이션
"""

current = 1  # 현재 층

while True:
    # 현재 층 표시 (-1이면 B1으로 표시)
    if current == -1:
        floor_name = "B1층"
    else:
        floor_name = str(current) + "층"
    print("현재 층: " + floor_name)

    target = int(input("이동할 층 입력 (0: 종료): "))

    # 종료
    if target == 0:
        print("엘리베이터를 종료합니다.")
        break

    # 범위 체크
    if target < -1 or target > 10:
        print("이동할 수 없는 층입니다. (-1 ~ 10)")
        print()
        continue

    # 같은 층
    if target == current:
        print("이미 해당 층에 있습니다.")
        print()
        continue

    # 이동 과정 출력
    if current == -1:
        output = "B1층"
    else:
        output = str(current) + "층"

    if target > current:
        # 올라가기
        floor = current + 1
        while floor <= target:
            if floor == 0:
                # 0층은 없으므로 건너뜀 (여기서는 -1 → 1로 직접 이동)
                floor = floor + 1
                continue
            if floor == -1:
                output = output + " → B1층"
            else:
                output = output + " → " + str(floor) + "층"
            floor = floor + 1
    else:
        # 내려가기
        floor = current - 1
        while floor >= target:
            if floor == 0:
                # 0층은 없으므로 건너뜀
                floor = floor - 1
                continue
            if floor == -1:
                output = output + " → B1층"
            else:
                output = output + " → " + str(floor) + "층"
            floor = floor - 1

    print(output)

    # 도착 메시지
    if target == -1:
        print("B1층에 도착했습니다.")
    else:
        print(str(target) + "층에 도착했습니다.")

    current = target
    print()
