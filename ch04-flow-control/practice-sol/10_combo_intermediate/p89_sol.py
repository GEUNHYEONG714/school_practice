"""
실습 89 풀이: 미니 스프레드시트
"""
n, m = input().split()
n = int(n)
m = int(m)

# 변수로 최대 3x3 격자 저장
v11 = 0
v12 = 0
v13 = 0
v21 = 0
v22 = 0
v23 = 0
v31 = 0
v32 = 0
v33 = 0

# 입력 및 출력
for r in range(1, n + 1):
    parts = input().split()
    c1 = int(parts[0])
    c2 = int(parts[1])
    c3 = 0
    if m >= 3:
        c3 = int(parts[2])

    if r == 1:
        v11 = c1
        v12 = c2
        v13 = c3
    elif r == 2:
        v21 = c1
        v22 = c2
        v23 = c3
    elif r == 3:
        v31 = c1
        v32 = c2
        v33 = c3

    # 격자 출력
    if m == 2:
        print(str(c1) + " " + str(c2))
    else:
        print(str(c1) + " " + str(c2) + " " + str(c3))

# 행 합
print()
print("행1 합: " + str(v11 + v12 + v13))
print("행2 합: " + str(v21 + v22 + v23))
if n >= 3:
    print("행3 합: " + str(v31 + v32 + v33))

# 열 합
print()
print("열1 합: " + str(v11 + v21 + v31))
print("열2 합: " + str(v12 + v22 + v32))
if m >= 3:
    print("열3 합: " + str(v13 + v23 + v33))
