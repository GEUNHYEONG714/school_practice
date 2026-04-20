"""
실습 52 풀이: 미니 RPG 전투
"""

player_hp = int(input("플레이어 HP: "))
monster_hp = int(input("몬스터 HP: "))
turn = 0

print("=== RPG 전투 시작! ===")
print("플레이어 HP:", player_hp, "| 몬스터 HP:", monster_hp)
print()

while player_hp > 0 and monster_hp > 0:
    turn += 1
    print("---", str(turn) + "턴 ---")

    # 플레이어 공격: 15~25 범위, 턴마다 변동
    p_damage = 15 + (turn * 7 + 3) % 11
    monster_hp -= p_damage
    print("플레이어 공격! 데미지:", p_damage, "| 몬스터 HP:", monster_hp)

    # 몬스터가 쓰러졌는지 확인 (쓰러지면 몬스터 공격 생략)
    if monster_hp <= 0:
        print()
        print("플레이어 승리! (" + str(turn) + "턴 만에 승리)")
        break

    # 몬스터 공격: 10~20 범위, 턴마다 변동 (13은 11과 서로소라 값이 실제로 변동)
    m_damage = 10 + (turn * 13 + 5) % 11
    player_hp -= m_damage
    print("몬스터 공격! 데미지:", m_damage, "| 플레이어 HP:", player_hp)
    print()

    # 플레이어가 쓰러졌는지 확인
    if player_hp <= 0:
        print("몬스터 승리... (플레이어 패배)")
        break
