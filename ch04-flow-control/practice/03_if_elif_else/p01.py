"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 1: 성적 등급

점수를 입력받아 등급을 출력하세요.
if/elif/else를 사용합니다.

[등급 기준]
90 이상: A
80 이상: B
70 이상: C
60 이상: D
60 미만: F
"""

score = int(input("점수를 입력하세요: "))

# 아래에 등급을 판정하여 출력하세요
level = ""
# 90점 이상
if score >= 90:
    level = "A"
# 80 이상: B
elif score >= 80:
    level = "B"
# 70 이상: C
elif score >= 70:
    level = "C"
# 60 이상: D
elif score >= 60:
    level = "D"
# 60 미만: F
else:
    level = "F"

# 출력
print(f"점수: {score}")
print(f"등급: {level}")
"""
[실행 결과 예시] (입력: 85)
점수: 85
등급: B
"""
