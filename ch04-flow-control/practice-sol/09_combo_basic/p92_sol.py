"""
실습 92 풀이: 숫자 빙고
"""

# 5개의 숫자를 입력받아 변수에 저장
n1 = int(input("숫자 1: "))
n2 = int(input("숫자 2: "))
n3 = int(input("숫자 3: "))
n4 = int(input("숫자 4: "))
n5 = int(input("숫자 5: "))

# 5x5 빙고판 출력
for row in range(5):
    line = ""
    for col in range(5):
        num = row * 5 + col + 1

        if col > 0:
            line += "\t"

        # 입력한 숫자와 일치하면 X 표시
        if num == n1 or num == n2 or num == n3 or num == n4 or num == n5:
            line += "X"
        else:
            line += str(num)

    print(line)
