"""
실습 49 풀이: 보물 찾기
"""

treasure = 42  # 보물 위치
attempt = 0
prev_diff = 100  # 이전 거리 (초기값: 큰 수)

print("=== 보물 찾기 ===")
print("1~100 사이에 보물이 숨겨져 있습니다!")
print()

while True:
    guess = int(input("위치를 추측하세요: "))
    attempt += 1

    # 절대값 계산 (abs 대신 if문 사용)
    diff = guess - treasure
    if diff < 0:
        diff = -diff

    # 정답 확인
    if diff == 0:
        print("보물을 찾았습니다! (시도: " + str(attempt) + "회)")
        print("축하합니다! 총 " + str(attempt) + "번 만에 보물을 찾았습니다!")
        break

    # 거리 힌트
    if diff <= 5:
        print("뜨거워! 아주 가까워요! (시도: " + str(attempt) + "회)")
    elif diff <= 15:
        print("따뜻해요! 근처에 있어요! (시도: " + str(attempt) + "회)")
    elif diff <= 30:
        print("미지근해요... (시도: " + str(attempt) + "회)")
    else:
        print("차가워요! 멀리 있어요! (시도: " + str(attempt) + "회)")

    # 이전보다 가까워졌는지 확인
    if diff < prev_diff:
        print("점점 가까워지고 있어요!")

    prev_diff = diff
