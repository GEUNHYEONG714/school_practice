"""
실습 50 풀이: 미니 텍스트 어드벤처
"""

hp = 100
has_key = 0     # 0: 열쇠 없음, 1: 열쇠 있음
current_room = 1
game_over = 0   # 0: 진행 중, 1: 종료

print("=== 미니 텍스트 어드벤처 ===")
print("당신은 신비한 던전에 들어왔습니다...")
print("HP:", hp)

while game_over == 0:
    print()

    # ===== 방 1: 시작의 방 =====
    if current_room == 1:
        print("--- 방 1: 시작의 방 ---")
        print("두 개의 문이 보입니다.")
        print("(1) 왼쪽 문  (2) 오른쪽 문")
        choice = int(input("선택: "))

        if choice == 1:
            # 왼쪽 문: 안전하게 방 2로 이동
            print("왼쪽 문을 열고 조심스럽게 들어갑니다.")
            current_room = 2
        elif choice == 2:
            # 오른쪽 문: 함정! HP -20
            hp -= 20
            print("오른쪽 문에 함정이 있었습니다! HP -20")
            print("HP:", hp)
            if hp <= 0:
                print("체력이 다했습니다... 게임 오버!")
                game_over = 1
            else:
                current_room = 2
        else:
            print("1 또는 2를 선택하세요.")

    # ===== 방 2: 보물의 방 =====
    elif current_room == 2:
        print("--- 방 2: 보물의 방 ---")
        print("낡은 상자가 하나 있습니다.")
        print("(1) 상자 열기  (2) 그냥 지나가기")
        choice = int(input("선택: "))

        if choice == 1:
            # 상자 열기: 열쇠 획득
            has_key = 1
            print("상자에서 열쇠를 발견했습니다!")
            current_room = 3
        elif choice == 2:
            # 그냥 지나가기
            print("상자를 무시하고 지나갑니다.")
            current_room = 3
        else:
            print("1 또는 2를 선택하세요.")

    # ===== 방 3: 최종 방 =====
    elif current_room == 3:
        print("--- 방 3: 최종 방 ---")
        print("거대한 잠긴 문이 보입니다.")

        if has_key == 1:
            # 열쇠가 있으면 탈출 성공
            print("열쇠로 문을 열었습니다!")
            print()
            print("축하합니다! 던전에서 탈출했습니다!")
            print("남은 HP:", hp)
            game_over = 1
        else:
            # 열쇠가 없으면 선택
            print("문이 잠겨 있습니다! 열쇠가 필요합니다.")
            print("(1) 돌아가기(방2)  (2) 문 부수기(HP-50)")
            choice = int(input("선택: "))

            if choice == 1:
                # 방 2로 돌아가기
                print("방 2로 돌아갑니다.")
                current_room = 2
            elif choice == 2:
                # 문 부수기
                hp -= 50
                print("문을 부쉈습니다! HP -50")
                print("HP:", hp)
                if hp <= 0:
                    print("체력이 다했습니다... 게임 오버!")
                    game_over = 1
                else:
                    print()
                    print("문을 부수고 탈출했습니다!")
                    print("남은 HP:", hp)
                    game_over = 1
            else:
                print("1 또는 2를 선택하세요.")
