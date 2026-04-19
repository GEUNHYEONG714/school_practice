"""
실습 85 풀이: 엘리베이터 최적화
"""
n = int(input())

# 최대 10명의 목적지를 변수에 저장
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
f7 = 0
f8 = 0
f9 = 0
f10 = 0

for i in range(n):
    floor = int(input())
    if i == 0:
        f1 = floor
    elif i == 1:
        f2 = floor
    elif i == 2:
        f3 = floor
    elif i == 3:
        f4 = floor
    elif i == 4:
        f5 = floor
    elif i == 5:
        f6 = floor
    elif i == 6:
        f7 = floor
    elif i == 7:
        f8 = floor
    elif i == 8:
        f9 = floor
    elif i == 9:
        f10 = floor

# 가장 높은 층 찾기
max_floor = f1
if n >= 2 and f2 > max_floor:
    max_floor = f2
if n >= 3 and f3 > max_floor:
    max_floor = f3
if n >= 4 and f4 > max_floor:
    max_floor = f4
if n >= 5 and f5 > max_floor:
    max_floor = f5
if n >= 6 and f6 > max_floor:
    max_floor = f6
if n >= 7 and f7 > max_floor:
    max_floor = f7
if n >= 8 and f8 > max_floor:
    max_floor = f8
if n >= 9 and f9 > max_floor:
    max_floor = f9
if n >= 10 and f10 > max_floor:
    max_floor = f10

# 2층부터 최고층까지 순서대로 확인
for floor in range(2, max_floor + 1):
    count = 0
    if f1 == floor:
        count += 1
    if n >= 2 and f2 == floor:
        count += 1
    if n >= 3 and f3 == floor:
        count += 1
    if n >= 4 and f4 == floor:
        count += 1
    if n >= 5 and f5 == floor:
        count += 1
    if n >= 6 and f6 == floor:
        count += 1
    if n >= 7 and f7 == floor:
        count += 1
    if n >= 8 and f8 == floor:
        count += 1
    if n >= 9 and f9 == floor:
        count += 1
    if n >= 10 and f10 == floor:
        count += 1

    if count > 0:
        print(str(floor) + "층: " + str(count) + "명 하차")

print("운행 완료 (최고층: " + str(max_floor) + "층)")
