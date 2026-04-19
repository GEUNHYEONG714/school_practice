"""
실습 97 풀이: 성적 히스토그램
"""

n = int(input("학생 수: "))

# 구간별 개수 (0~9, 10~19, ..., 90~100) -> 10개 구간
c0 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0

for i in range(n):
    score = int(input())
    # 100점은 90~100 구간에 포함
    g = score // 10
    if g >= 10:
        g = 9
    if g == 0:
        c0 += 1
    elif g == 1:
        c1 += 1
    elif g == 2:
        c2 += 1
    elif g == 3:
        c3 += 1
    elif g == 4:
        c4 += 1
    elif g == 5:
        c5 += 1
    elif g == 6:
        c6 += 1
    elif g == 7:
        c7 += 1
    elif g == 8:
        c8 += 1
    elif g == 9:
        c9 += 1

# 0이 아닌 구간만 출력
if c0 > 0:
    print("0~9:", "#" * c0)
if c1 > 0:
    print("10~19:", "#" * c1)
if c2 > 0:
    print("20~29:", "#" * c2)
if c3 > 0:
    print("30~39:", "#" * c3)
if c4 > 0:
    print("40~49:", "#" * c4)
if c5 > 0:
    print("50~59:", "#" * c5)
if c6 > 0:
    print("60~69:", "#" * c6)
if c7 > 0:
    print("70~79:", "#" * c7)
if c8 > 0:
    print("80~89:", "#" * c8)
if c9 > 0:
    print("90~100:", "#" * c9)
