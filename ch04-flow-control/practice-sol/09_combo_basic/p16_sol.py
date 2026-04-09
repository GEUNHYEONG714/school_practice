"""
실습 풀이: N명 평균 점수
"""

n = int(input("학생 수를 입력하세요: "))

total = 0  # 점수 합계

# N명의 점수를 입력받아 누적
for i in range(1, n + 1):
    score = int(input(str(i) + "번 학생 점수: "))
    total += score

# 평균 = 합계 / 인원 수
average = total / n
print("평균 점수:", average)
