"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 4: 택시비 계산

거리(km)와 시간대(야간 여부)를 입력받아 택시비를 계산합니다.

- 기본요금: 4800원 (2km까지 포함)
- 추가요금: 2km 초과 시 1km당 1000원
- 야간 할증(22시~06시): 총 요금의 20% 추가

힌트: 거리 계산 후 야간 여부를 추가 판단합니다.
"""

distance = float(input("거리를 입력하세요 (km): "))
hour = int(input("현재 시간을 입력하세요 (0~23): "))

# 아래에 택시비를 계산하는 코드를 작성하세요

# 기본 요금
base_fare = 4800
print(f"기본요금: {base_fare}원")

# 추가 요금 계산
if distance > 2:
    extra_fare = int((distance - 2) * 1000)
else:
    extra_fare = 0
print(f"추가요금: {extra_fare}원")

# 총 요금 계산
total = base_fare + extra_fare

# 야간 할증 확인
if hour >= 22 or hour < 6:
    night_fare = int(total * 0.2)
    print(f"야간 할증 (20%): {night_fare}원")
    total = total + night_fare

# 최종 요금 출력
print(f"총 택시비: {total}원")



"""
[실행 결과 예시]
거리를 입력하세요 (km): 5
현재 시간을 입력하세요 (0~23): 14
기본요금: 4800원
추가요금: 3000원
총 택시비: 7800원

거리를 입력하세요 (km): 5
현재 시간을 입력하세요 (0~23): 23
기본요금: 4800원
추가요금: 3000원
야간 할증 (20%): 1560원
총 택시비: 9360원
"""
