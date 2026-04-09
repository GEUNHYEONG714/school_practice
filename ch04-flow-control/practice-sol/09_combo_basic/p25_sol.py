"""
실습 25 풀이: 별 등급 표시
"""

n = int(input("학생 수를 입력하세요: "))

for i in range(1, n + 1):
    score = int(input(str(i) + "번 학생 점수: "))

    # 점수 구간에 따라 별 개수 결정
    if score >= 90:
        stars = "★★★★★"
    elif score >= 80:
        stars = "★★★★"
    elif score >= 70:
        stars = "★★★"
    elif score >= 60:
        stars = "★★"
    else:
        stars = "★"

    print(str(i) + "번 학생:", stars)
