"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 47: 주차 요금 계산

입차 시간과 출차 시간을 입력받아 주차 요금을 계산합니다.
- 기본 요금: 30분 이하 2000원
- 추가 요금: 30분 초과 시 10분당 500원
- 시간은 분 단위로 입력 (예: 90분)

힌트: if/else와 산술 연산을 조합합니다.
"""

print("=== 주차 요금 계산기 ===")
enter_time = int(input("입차 시간(분): "))
exit_time = int(input("출차 시간(분): "))

# 주차 시간 계산
parked = exit_time - enter_time

# 아래에 요금 계산 코드를 작성하세요
print("=== 주차 요금 계산기 ===")
enter_time = int(input("입차 시간(분): "))
exit_time = int(input("출차 시간(분): "))

# 주차 시간 계산
parked = exit_time - enter_time

# 기본 요금
base_fee = 2000

# 추가 요금 초기화
extra_fee = 0

# 주차 시간이 30분을 초과하는 경우
if parked > 30:
    # 30분을 초과한 시간 계산
    extra_minutes = parked - 30

    # 10분당 500원 계산
    extra_fee = (extra_minutes // 10) * 500

    # 10분이 안 되는 남은 시간도 요금 추가
    if extra_minutes % 10 > 0:
        extra_fee += 500

    print(f"추가 시간: {extra_minutes}분")

# 주차 시간 출력
print(f"주차 시간: {parked}분")
# 기본 요금 출력
print(f"기본 요금: {base_fee}원")
# 추가 요금 출력
print(f"추가 요금: {extra_fee}원")

# 총 요금 계산
total = base_fee + extra_fee
print(f"총 요금: {total}원")

"""
[실행 결과 예시]
=== 주차 요금 계산기 ===
입차 시간(분): 0
출차 시간(분): 90
주차 시간: 90분
기본 요금: 2000원
추가 시간: 60분
추가 요금: 3000원
총 요금: 5000원

[실행 결과 예시 2]
=== 주차 요금 계산기 ===
입차 시간(분): 0
출차 시간(분): 20
주차 시간: 20분
기본 요금: 2000원
추가 요금: 0원
총 요금: 2000원
"""
