"""
실습 23 풀이: 합격자 수 세기
"""

n = int(input("학생 수를 입력하세요: "))
count = 0  # 합격자 수

# N명의 점수를 입력받아 60점 이상이면 합격
for i in range(1, n + 1):
    score = int(input(str(i) + "번 학생 점수: "))

    # 60점 이상이면 합격자 수 증가
    if score >= 60:
        count += 1

print("합격자 수:", count)
