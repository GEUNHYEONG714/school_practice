"""
실습 53 풀이: 체력 테스트 등급
"""

count = int(input("윗몸일으키기 횟수를 입력하세요: "))

# 횟수에 따라 등급 판정
if count >= 60:
    grade = "A"
elif count >= 45:
    grade = "B"
elif count >= 30:
    grade = "C"
elif count >= 15:
    grade = "D"
else:
    grade = "F"

print("횟수: " + str(count) + "회 → 등급: " + grade)
