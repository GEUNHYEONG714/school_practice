"""
실습 5 풀이: 성적 평가
"""

score = int(input("점수를 입력하세요 (0~100): "))
attendance = int(input("출석률을 입력하세요 (0~100): "))

# 점수에 따라 등급 판별
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("등급:", grade)

# 수료 여부 판단
if grade == "F":
    # 성적 미달
    print("미수료 - 성적 미달 (60점 이상 필요)")
elif attendance < 80:
    # 출석률 부족
    print("미수료 - 출석률 부족 (80% 이상 필요)")
else:
    # 성적과 출석률 모두 충족
    print("수료를 축하합니다!")
