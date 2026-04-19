"""
실습 68 풀이: 점프 게임
"""

n = int(input("N을 입력하세요: "))
jumps = input("점프력을 입력하세요: ")

parts = jumps.split()
max_reach = 0   # 도달 가능한 최대 인덱스
idx = 0

for p in parts:
    val = int(p)

    # 현재 인덱스에 도달할 수 없으면 종료
    if idx > max_reach:
        break

    # 최대 도달 범위 갱신
    if idx + val > max_reach:
        max_reach = idx + val

    idx += 1

if max_reach >= n - 1:
    print("YES")
else:
    print("NO")
