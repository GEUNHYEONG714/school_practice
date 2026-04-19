"""
실습 95 풀이: 달력 출력
"""

start_day = int(input("시작 요일(1=월~7=일): "))
last_date = int(input("마지막 날짜: "))

# 헤더 출력
print("월  화  수  목  금  토  일")

# 시작 요일 전 빈칸 출력
line = ""
for i in range(1, start_day):
    line += "    "

# 날짜 출력
pos = start_day  # 현재 요일 위치 (1~7)
for day in range(1, last_date + 1):
    # 2자리 오른쪽 정렬
    line += str(day).rjust(2)

    if pos == 7:
        # 일요일이면 줄 출력 후 초기화
        print(line)
        line = ""
        pos = 1
    else:
        # 다음 칸을 위한 구분자 (공백 2칸)
        line += "  "
        pos += 1

# 마지막 줄 출력 (일요일에 끝나지 않은 경우)
if line != "":
    print(line.rstrip())
