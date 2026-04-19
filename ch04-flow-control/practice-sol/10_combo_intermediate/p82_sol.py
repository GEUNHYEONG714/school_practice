"""
실습 82 풀이: 볼링 점수 (간소화)
"""
n = int(input())
total = 0

for i in range(1, n + 1):
    line = input().split()
    ball1 = int(line[0])
    ball2 = int(line[1])

    score = ball1 + ball2

    if ball1 == 10:
        # 스트라이크: +5 보너스
        score += 5
    elif ball1 + ball2 == 10:
        # 스페어: +3 보너스
        score += 3

    total += score
    print("프레임 " + str(i) + ": " + str(score) + "점")

print("총점: " + str(total) + "점")
