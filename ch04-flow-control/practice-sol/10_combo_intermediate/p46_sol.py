"""
실습 46 풀이: 동전 뒤집기 게임
"""

round_num = 1
streak = 0       # 현재 연속 정답
best_streak = 0  # 최대 연속 정답 기록
total_correct = 0  # 총 정답 수
total_games = 0    # 총 게임 수

print("=== 동전 뒤집기 게임 ===")
print("앞(1) 또는 뒤(2)를 맞춰보세요! (종료: 0)")
print()

while True:
    guess = int(input("[라운드 " + str(round_num) + "] 앞(1)/뒤(2) 입력: "))

    # 종료 조건
    if guess == 0:
        break

    total_games += 1

    # 동전 결과 결정 (고정 패턴)
    # 기본: 홀수 라운드→앞(1), 짝수 라운드→뒤(2)
    # 예외: 3의 배수 라운드는 반대
    if round_num % 2 == 1:
        coin = 1  # 홀수: 앞
    else:
        coin = 2  # 짝수: 뒤

    # 3의 배수이면 반전
    if round_num % 3 == 0:
        if coin == 1:
            coin = 2
        else:
            coin = 1

    # 동전 이름
    if coin == 1:
        coin_name = "앞"
    else:
        coin_name = "뒤"

    # 정답 확인
    if guess == coin:
        streak += 1
        total_correct += 1
        print("동전: " + coin_name + "! 정답! (연속 " + str(streak) + "회)")
        # 최대 연속 기록 갱신
        if streak > best_streak:
            best_streak = streak
    else:
        streak = 0
        print("동전: " + coin_name + "! 틀렸습니다! (연속 기록 초기화)")

    round_num += 1

# 게임 결과 출력
print()
print("=== 게임 결과 ===")
print("총 게임: " + str(total_games) + "회")
print("정답: " + str(total_correct) + "회")
print("최대 연속 정답: " + str(best_streak) + "회")
