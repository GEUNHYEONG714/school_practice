"""
실습 80 풀이: 별 원형
"""
n = int(input())
R = n // 2

# 경계값 계산 (소수 비교를 위해 4배로 스케일)
low = (2 * R - 1) * (2 * R - 1)   # (R-0.5)^2 * 4 → 비교용
high = (2 * R + 1) * (2 * R + 1)  # (R+0.5)^2 * 4 → 비교용

for r in range(n):
    # 마지막 * 위치 찾기
    last_star = -1
    for c in range(n):
        dr = r - R
        dc = c - R
        dist_sq_4 = 4 * (dr * dr + dc * dc)  # 4배 스케일
        if dist_sq_4 >= low and dist_sq_4 <= high:
            last_star = c

    line = ""
    for c in range(last_star + 1):
        dr = r - R
        dc = c - R
        dist_sq_4 = 4 * (dr * dr + dc * dc)
        if dist_sq_4 >= low and dist_sq_4 <= high:
            line += "*"
        else:
            line += " "
    print(line)
