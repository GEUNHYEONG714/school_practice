"""
실습 86 풀이: 학점 계산기 (가중 평균)
"""
n = int(input())
total_score = 0.0  # 학점점수 * 이수학점의 합
total_credit = 0   # 총 이수학점

for i in range(1, n + 1):
    line = input().split()
    grade = line[0]
    credit = int(line[1])

    # 학점별 점수 변환
    point = 0.0
    if grade == "A+":
        point = 4.5
    elif grade == "A":
        point = 4.0
    elif grade == "B+":
        point = 3.5
    elif grade == "B":
        point = 3.0
    elif grade == "C+":
        point = 2.5
    elif grade == "C":
        point = 2.0
    elif grade == "D+":
        point = 1.5
    elif grade == "D":
        point = 1.0
    else:  # F
        point = 0.0

    total_score += point * credit
    total_credit += credit
    print("과목" + str(i) + ": " + grade + " (" + str(credit) + "학점)")

gpa = total_score / total_credit
# 소수점 둘째 자리 출력
gpa_str = str(int(gpa * 100 + 0.5) / 100)
# format 대신 직접 처리
print("GPA: %.2f" % gpa)
