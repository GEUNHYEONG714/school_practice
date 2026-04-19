"""
실습 95 풀이: 스네이크 이동
"""
row = 2
col = 2
path = "(" + str(row) + "," + str(col) + ")"

for i in range(5):
    direction = input()
    nr = row
    nc = col

    if direction == "U":
        nr = row - 1
    elif direction == "D":
        nr = row + 1
    elif direction == "L":
        nc = col - 1
    elif direction == "R":
        nc = col + 1

    # 범위 확인 (0~4)
    if 0 <= nr <= 4 and 0 <= nc <= 4:
        row = nr
        col = nc

    path += "->(" + str(row) + "," + str(col) + ")"

print(str(row) + " " + str(col))
print(path)
