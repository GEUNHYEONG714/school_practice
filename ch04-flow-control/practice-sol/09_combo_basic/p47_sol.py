"""
실습 47 풀이: 주차 요금 계산
"""

print("=== 주차 요금 계산기 ===")
enter_time = int(input("입차 시간(분): "))
exit_time = int(input("출차 시간(분): "))

# 주차 시간 계산
parked = exit_time - enter_time
print("주차 시간:", str(parked) + "분")

# 기본 요금
base_fee = 2000
print("기본 요금:", str(base_fee) + "원")

# 추가 요금 계산
if parked <= 30:
    # 30분 이하: 추가 요금 없음
    extra_fee = 0
    print("추가 요금:", str(extra_fee) + "원")
else:
    # 30분 초과: 10분당 500원
    extra_minutes = parked - 30
    print("추가 시간:", str(extra_minutes) + "분")
    extra_fee = (extra_minutes // 10) * 500
    # 10분 미만 나머지도 청구
    if extra_minutes % 10 > 0:
        extra_fee += 500
    print("추가 요금:", str(extra_fee) + "원")

# 총 요금
total = base_fee + extra_fee
print("총 요금:", str(total) + "원")
