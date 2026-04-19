"""
실습 77 풀이: 별 계단
"""
n = int(input())

for i in range(1, n + 1):
    line = ""
    # 앞 공백
    for s in range(i - 1):
        line += " "
    # 별
    for s in range(i):
        line += "*"
    print(line)
