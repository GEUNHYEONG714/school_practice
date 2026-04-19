"""
실습 57 풀이: 수영장 입장
"""

age = int(input("나이를 입력하세요: "))
time_slot = input("시간대를 입력하세요 (오전/오후): ")

# 나이별 기본 요금 결정
if age <= 7:
    fee = 0
elif age <= 13:
    fee = 3000
elif age <= 18:
    fee = 5000
else:
    fee = 8000

# 오후 시간대이면 50% 할증
if time_slot == "오후":
    fee = int(fee * 1.5)

print("나이: " + str(age) + "세 | 시간대: " + time_slot)
print("입장료: " + str(fee) + "원")
