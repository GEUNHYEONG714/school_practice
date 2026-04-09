"""
실습 13 풀이: 미니 성적 관리
"""

total = 0  # 점수 합계
best = 0   # 최고점 (가장 높은 점수를 저장)

# 5명의 점수를 입력받는다
for i in range(1, 6):
    score = int(input(str(i) + "번 학생 점수: "))

    total += score  # 합계에 누적

    # 현재 입력된 점수가 지금까지의 최고점보다 크면 갱신
    if score > best:
        best = score

# 평균 = 합계 / 인원 수
average = total / 5
print("평균:", average)
print("최고점:", best)
