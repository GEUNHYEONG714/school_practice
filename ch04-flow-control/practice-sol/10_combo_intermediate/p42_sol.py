"""
실습 42 풀이: 행운의 룰렛
"""

# 정답
answer = 7
max_chance = 3

print("=== 행운의 룰렛 ===")
print("1~10 중 숫자를 맞춰보세요! (기회: " + str(max_chance) + "번)")
print()

chance = 1
found = 0  # 정답 맞춤 여부

while chance <= max_chance:
    guess = int(input("[" + str(chance) + "번째 시도] 숫자 입력: "))

    # 정답 확인
    if guess == answer:
        print("정답입니다! 축하합니다!")
        found = 1
        break

    # 근접도 계산 (절대값)
    diff = guess - answer
    if diff < 0:
        diff = -diff

    # 근접도 힌트
    remaining = max_chance - chance
    if diff == 1:
        print("아주 가까워요! (뜨거워!) (남은 기회: " + str(remaining) + "번)")
    elif diff <= 3:
        print("가까워요! (따뜻해요) (남은 기회: " + str(remaining) + "번)")
    else:
        print("멀어요... (차가워요) (남은 기회: " + str(remaining) + "번)")

    chance += 1

# 기회를 모두 사용한 경우
if found == 0:
    print("기회를 모두 사용했습니다. 정답은 " + str(answer) + "이었습니다.")
