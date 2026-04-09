"""
실습 4 풀이: 택시비 계산
"""

distance = float(input("거리를 입력하세요 (km): "))
hour = int(input("현재 시간을 입력하세요 (0~23): "))

# 기본요금 설정
base_fare = 4800
print("기본요금:", str(base_fare) + "원")

# 추가요금 계산 (2km 초과분)
if distance > 2:
    extra_fare = int((distance - 2) * 1000)
else:
    extra_fare = 0
print("추가요금:", str(extra_fare) + "원")

# 기본 합계
total = base_fare + extra_fare

# 야간 할증 판단 (22시~23시 또는 0시~5시)
if hour >= 22 or hour < 6:
    night_extra = int(total * 0.2)
    print("야간 할증 (20%):", str(night_extra) + "원")
    total = total + night_extra

# 최종 요금 출력
print("총 택시비:", str(total) + "원")
