"""
실습 93 풀이: 카드 게임 (블랙잭 간소)
"""
line = input().split()
a, b, c = int(line[0]), int(line[1]), int(line[2])

best = -1  # 21 이하 최대합

# 1장 조합: a, b, c
if a <= 21 and a > best:
    best = a
if b <= 21 and b > best:
    best = b
if c <= 21 and c > best:
    best = c

# 2장 조합: a+b, a+c, b+c
ab = a + b
ac = a + c
bc = b + c
if ab <= 21 and ab > best:
    best = ab
if ac <= 21 and ac > best:
    best = ac
if bc <= 21 and bc > best:
    best = bc

# 3장 조합: a+b+c
abc = a + b + c
if abc <= 21 and abc > best:
    best = abc

print(best)
