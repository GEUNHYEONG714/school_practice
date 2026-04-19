"""
실습 102 풀이: 시간표 출력
"""

n = int(input("과목 수: "))

# 6교시 각각에 대한 과목명 저장
s1 = "-"
s2 = "-"
s3 = "-"
s4 = "-"
s5 = "-"
s6 = "-"

for i in range(n):
    line = input()
    parts = line.split()
    name = parts[0]
    start = int(parts[1])
    end = int(parts[2])

    # 시작교시~끝교시에 과목 배정 (먼저 입력된 과목 우선)
    for p in range(start, end + 1):
        if p == 1 and s1 == "-":
            s1 = name
        elif p == 2 and s2 == "-":
            s2 = name
        elif p == 3 and s3 == "-":
            s3 = name
        elif p == 4 and s4 == "-":
            s4 = name
        elif p == 5 and s5 == "-":
            s5 = name
        elif p == 6 and s6 == "-":
            s6 = name

# 표 출력
print("교시 | 과목")
print("-----|------")
print("1교시 | " + s1)
print("2교시 | " + s2)
print("3교시 | " + s3)
print("4교시 | " + s4)
print("5교시 | " + s5)
print("6교시 | " + s6)
