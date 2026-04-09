"""
실습 풀이: 구간별 카운트
"""

a_count = 0  # 90점 이상
b_count = 0  # 80점 이상
c_count = 0  # 70점 이상
d_count = 0  # 70점 미만

# 10명의 점수를 입력받으며 구간별로 분류
for i in range(1, 11):
    score = int(input(str(i) + "번 학생 점수: "))

    if score >= 90:
        a_count += 1
    elif score >= 80:
        b_count += 1
    elif score >= 70:
        c_count += 1
    else:
        d_count += 1

print("90점 이상:", str(a_count) + "명")
print("80점 이상:", str(b_count) + "명")
print("70점 이상:", str(c_count) + "명")
print("70점 미만:", str(d_count) + "명")
