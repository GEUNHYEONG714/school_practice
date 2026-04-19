"""
실습 94 풀이: 미니 체스 (나이트 이동)
"""
line = input().split()
r, c = int(line[0]), int(line[1])

# 8가지 이동을 행 오름차순, 열 오름차순으로 직접 나열
# (-2,-1), (-2,+1), (-1,-2), (-1,+2), (+1,-2), (+1,+2), (+2,-1), (+2,+1)

nr = r - 2
nc = c - 1
if 0 <= nr <= 7 and 0 <= nc <= 7:
    print(str(nr) + " " + str(nc))

nr = r - 2
nc = c + 1
if 0 <= nr <= 7 and 0 <= nc <= 7:
    print(str(nr) + " " + str(nc))

nr = r - 1
nc = c - 2
if 0 <= nr <= 7 and 0 <= nc <= 7:
    print(str(nr) + " " + str(nc))

nr = r - 1
nc = c + 2
if 0 <= nr <= 7 and 0 <= nc <= 7:
    print(str(nr) + " " + str(nc))

nr = r + 1
nc = c - 2
if 0 <= nr <= 7 and 0 <= nc <= 7:
    print(str(nr) + " " + str(nc))

nr = r + 1
nc = c + 2
if 0 <= nr <= 7 and 0 <= nc <= 7:
    print(str(nr) + " " + str(nc))

nr = r + 2
nc = c - 1
if 0 <= nr <= 7 and 0 <= nc <= 7:
    print(str(nr) + " " + str(nc))

nr = r + 2
nc = c + 1
if 0 <= nr <= 7 and 0 <= nc <= 7:
    print(str(nr) + " " + str(nc))
