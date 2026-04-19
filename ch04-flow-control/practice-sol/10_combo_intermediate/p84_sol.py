"""
실습 84 풀이: 신호등 시뮬레이션
"""
t = int(input())
g, y, r = input().split()
g = int(g)
y = int(y)
r = int(r)

cycle = g + y + r  # 한 주기 길이

for sec in range(t):
    pos = sec % cycle  # 현재 주기 내 위치
    if pos < g:
        signal = "초록"
    elif pos < g + y:
        signal = "노랑"
    else:
        signal = "빨강"
    print(str(sec) + "초: " + signal)
