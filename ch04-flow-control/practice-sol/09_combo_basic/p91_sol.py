"""
실습 91 풀이: 배열 출력
"""

n = int(input("정수를 입력하세요: "))

num = 1  # 출력할 숫자

for i in range(n):
    line = ""
    for j in range(n):
        if j > 0:
            line += "\t"
        line += str(num)
        num += 1
    print(line)
