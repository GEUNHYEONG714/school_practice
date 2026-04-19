"""
실습 89 풀이: 숫자 야구 (간단)
"""

# 정답: 37
answer_ten = 3  # 십의 자리
answer_one = 7  # 일의 자리

count = 0

while True:
    guess = int(input())
    count += 1

    guess_ten = guess // 10  # 십의 자리
    guess_one = guess % 10   # 일의 자리

    # 정답이면 종료
    if guess_ten == answer_ten and guess_one == answer_one:
        print("정답!", str(count) + "번 만에 맞춤")
        break

    # 스트라이크와 볼 계산
    strike = 0
    ball = 0

    # 같은 자리에 같은 숫자 → 스트라이크
    if guess_ten == answer_ten:
        strike += 1
    if guess_one == answer_one:
        strike += 1

    # 다른 자리에 같은 숫자 → 볼
    if guess_ten == answer_one:
        ball += 1
    if guess_one == answer_ten:
        ball += 1

    if strike == 0 and ball == 0:
        print("아웃")
    else:
        print(str(strike) + "스트라이크 " + str(ball) + "볼")
