"""
실습 48 풀이: 숫자 맞추기 업다운 게임
"""

answer = 42  # 정답 (미리 설정)
tries = 0

print("=== 숫자 맞추기 게임 (1~100) ===")

while True:
    guess = int(input("숫자를 입력하세요: "))
    tries += 1  # 시도 횟수 증가

    # 정답 비교
    if guess < answer:
        print("UP!")      # 더 큰 수를 입력해야 함
    elif guess > answer:
        print("DOWN!")    # 더 작은 수를 입력해야 함
    else:
        print("정답입니다! 시도 횟수:", str(tries) + "번")
        break
