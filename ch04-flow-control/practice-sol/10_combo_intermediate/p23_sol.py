"""
실습 23 풀이: 지그재그 패턴
"""

n = int(input("줄 수 입력: "))
m = int(input("한 줄 숫자 개수 입력: "))

num = 1  # 출력할 숫자 (1부터 시작)

for i in range(1, n + 1):
    # 한 줄에 출력할 숫자들을 문자열로 구성
    line = ""
    for j in range(m):
        if j > 0:
            line = line + " "
        line = line + str(num)
        num += 1

    # 짝수 줄이면 오른쪽 정렬 (전체 너비 = m * 2)
    if i % 2 == 0:
        # 오른쪽 정렬을 위해 앞에 공백 추가
        width = m * 2
        spaces = width - len(line)
        for s in range(spaces):
            print(" ", end="")

    print(line)
