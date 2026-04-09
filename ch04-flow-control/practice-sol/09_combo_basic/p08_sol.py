"""
실습 8 풀이: 놀이공원 입장료
"""

age = int(input("나이를 입력하세요: "))
group_count = int(input("인원 수를 입력하세요: "))

# 나이별 기본 입장료 결정
if age <= 3:
    price = 0
elif age <= 12:
    price = 15000
elif age <= 18:
    price = 20000
elif age <= 64:
    price = 30000
else:
    price = 10000

print("기본 입장료:", str(price) + "원")

# 단체 할인 판단 (10명 이상)
if group_count >= 10:
    print("단체 할인 적용 (20%)!")
    price = int(price * 0.8)
    print("1인 할인가:", str(price) + "원")

# 총 입장료 계산
total = price * group_count
print("총 입장료:", str(total) + "원")
