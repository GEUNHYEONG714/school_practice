"""
실습 38 풀이: 자리 배치
"""

n = int(input("인원 수: "))
m = int(input("열 수: "))

# 총 행 수 계산
if n % m == 0:
    total_rows = n // m
else:
    total_rows = n // m + 1

# 배치된 인원 카운트
placed = 0

row = 1
while row <= total_rows:
    # 행 시작
    line = "[" + str(row) + "행] "

    col = 1
    while col <= m:
        # N명 모두 배치되면 중단
        if placed >= n:
            break

        if col > 1:
            line = line + "  "  # 좌석 사이 간격
        line = line + str(row) + "-" + str(col)
        placed = placed + 1
        col = col + 1

    print(line)
    row = row + 1

print("총 " + str(total_rows) + "행 배치 완료 (" + str(n) + "명)")
