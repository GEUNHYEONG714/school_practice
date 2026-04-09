"""
실습 4 풀이: 숫자 맞추기 게임
"""

answer = 42

# while True: 조건이 항상 참이므로 무한히 반복된다
# 정답을 맞출 때 break로 빠져나온다
while True:
    guess = int(input("숫자를 입력하세요: "))

    # 입력한 수와 정답을 비교하여 힌트 제공
    if guess < answer:
        print("더 큰 수를 입력하세요")
    elif guess > answer:
        print("더 작은 수를 입력하세요")
    else:
        # guess == answer인 경우 (위 두 조건이 모두 거짓)
        print("정답입니다!")
        break  # 반복 종료
