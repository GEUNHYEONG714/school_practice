"""
실습 83 풀이: 비행기 좌석 배치
"""
n = int(input())

# 좌석 정보를 변수로 저장 (최대 9행 * 6열 = 54개 → 플래그 변수)
# 행-열 조합을 숫자로 인코딩: row*10 + col (A=0~F=5)
# 최대 10개 좌석 입력이므로 변수 10개로 저장
s1 = -1
s2 = -1
s3 = -1
s4 = -1
s5 = -1
s6 = -1
s7 = -1
s8 = -1
s9 = -1
s10 = -1
max_row = 0

for i in range(n):
    seat = input()
    row = int(seat[0])
    col_ch = seat[1]
    # A=0, B=1, C=2, D=3, E=4, F=5
    col = 0
    if col_ch == "B":
        col = 1
    elif col_ch == "C":
        col = 2
    elif col_ch == "D":
        col = 3
    elif col_ch == "E":
        col = 4
    elif col_ch == "F":
        col = 5

    code = row * 10 + col
    if i == 0:
        s1 = code
    elif i == 1:
        s2 = code
    elif i == 2:
        s3 = code
    elif i == 3:
        s4 = code
    elif i == 4:
        s5 = code
    elif i == 5:
        s6 = code
    elif i == 6:
        s7 = code
    elif i == 7:
        s8 = code
    elif i == 8:
        s9 = code
    elif i == 9:
        s10 = code

    if row > max_row:
        max_row = row

# 헤더 출력
print("  A B C   D E F")

# 각 행 출력
for r in range(1, max_row + 1):
    line = str(r)
    for c in range(6):
        if c == 3:
            line += "  "  # 통로
        code = r * 10 + c
        occupied = 0
        if code == s1 or code == s2 or code == s3 or code == s4 or code == s5:
            occupied = 1
        if code == s6 or code == s7 or code == s8 or code == s9 or code == s10:
            occupied = 1

        if occupied == 1:
            line += " O"
        else:
            line += " ."
    print(line)
