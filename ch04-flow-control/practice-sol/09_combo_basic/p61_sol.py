"""
실습 61 풀이: 알바 급여
"""

wage = int(input("시급(원)을 입력하세요: "))
hours = int(input("근무시간을 입력하세요: "))
start = int(input("시작 시각을 입력하세요: "))

# 근무 종료 시각
end = start + hours

# 22시 이후 야간 근무시간 계산
if end <= 22:
    night_hours = 0
elif start >= 22:
    night_hours = hours
else:
    night_hours = end - 22

# 일반 근무시간
normal_hours = hours - night_hours

# 기본급 = 일반시간 * 시급 + 야간시간 * 시급 * 1.5
base_pay = int(normal_hours * wage + night_hours * wage * 1.5)

# 주휴수당 = 기본급의 20%
weekly_pay = int(base_pay * 0.2)

# 총 급여
total = base_pay + weekly_pay

print("시급: " + str(wage) + "원 | 근무: " + str(hours) + "시간 (" + str(start) + "시 시작)")
print("기본급: " + str(base_pay) + "원")
print("주휴수당: " + str(weekly_pay) + "원")
print("총 급여: " + str(total) + "원")
