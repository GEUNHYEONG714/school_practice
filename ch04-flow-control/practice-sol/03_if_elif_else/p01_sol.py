"""
실습 2 풀이: 성적 등급
"""

score = int(input("점수를 입력하세요: "))

# elif는 위에서부터 순서대로 검사한다
# 예: 85점이면 score >= 90은 거짓 → score >= 80은 참 → "B"
# 이미 위에서 90 이상을 걸렀으므로, 80 이상만 확인하면 된다
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

print("점수:", score)
print("등급:", grade)
