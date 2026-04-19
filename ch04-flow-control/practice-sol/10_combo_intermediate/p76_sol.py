"""
실습 76 풀이: 숫자 지그재그 삼각형
"""
n = int(input())
num = 1  # 연속 증가하는 숫자

for i in range(1, n + 1):
    start = num  # 이 행의 시작 숫자
    num += i     # 다음 행 시작 숫자로 이동

    if i % 2 == 1:
        # 홀수 행: 정순 출력
        line = ""
        for j in range(i):
            if j > 0:
                line += " "
            line += str(start + j)
        print(line)
    else:
        # 짝수 행: 역순 출력
        line = ""
        for j in range(i):
            if j > 0:
                line += " "
            line += str(start + i - 1 - j)
        print(line)
