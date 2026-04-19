"""
실습 73 풀이: 숫자 모래시계
"""
n = int(input())
mid = n // 2  # 가운데 행 인덱스

for i in range(n):
    # 현재 행에서 줄어든 정도 계산
    if i <= mid:
        shrink = i
    else:
        shrink = n - 1 - i

    # 앞 공백 (2칸씩)
    line = ""
    for s in range(shrink):
        line += "  "

    # 숫자 출력: shrink+1 부터 n-shrink 까지
    start = shrink + 1
    end = n - shrink
    for j in range(start, end + 1):
        if j > start:
            line += " "
        line += str(j)
    print(line)
