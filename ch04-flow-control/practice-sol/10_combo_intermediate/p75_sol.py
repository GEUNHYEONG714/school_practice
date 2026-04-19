"""
실습 75 풀이: 별 피라미드 (가운데 정렬)
"""
n = int(input())

for i in range(1, n + 1):
    # 앞 공백
    line = ""
    for s in range(n - i):
        line += " "
    # 별
    for s in range(2 * i - 1):
        line += "*"
    print(line)
