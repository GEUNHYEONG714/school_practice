"""
실습 41 풀이: 숫자 야구
"""

# 정답 (3자리, 중복 없는 숫자)
answer_d1 = 3  # 백의 자리
answer_d2 = 1  # 십의 자리
answer_d3 = 7  # 일의 자리

attempt = 0  # 시도 횟수
strike = 0

# 3스트라이크가 나올 때까지 반복
while strike != 3:
    guess = int(input("3자리 숫자를 입력하세요: "))
    attempt += 1

    # 입력값에서 각 자릿수 분리
    g1 = guess // 100       # 백의 자리
    g2 = (guess // 10) % 10 # 십의 자리
    g3 = guess % 10          # 일의 자리

    strike = 0
    ball = 0

    # 스트라이크 판정 (같은 자리, 같은 숫자)
    if g1 == answer_d1:
        strike += 1
    if g2 == answer_d2:
        strike += 1
    if g3 == answer_d3:
        strike += 1

    # 볼 판정 (다른 자리, 같은 숫자)
    # g1과 정답의 2,3번째 비교
    if g1 != answer_d1:
        if g1 == answer_d2 or g1 == answer_d3:
            ball += 1
    # g2와 정답의 1,3번째 비교
    if g2 != answer_d2:
        if g2 == answer_d1 or g2 == answer_d3:
            ball += 1
    # g3와 정답의 1,2번째 비교
    if g3 != answer_d3:
        if g3 == answer_d1 or g3 == answer_d2:
            ball += 1

    # 결과 출력
    if strike == 3:
        print("3스트라이크! 정답입니다!")
        print("총 " + str(attempt) + "번 만에 맞추셨습니다!")
    elif strike == 0 and ball == 0:
        print("아웃!")
    else:
        print(str(strike) + "스트라이크 " + str(ball) + "볼")
