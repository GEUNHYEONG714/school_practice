"""
실습 5 풀이: 영화 요금 계산
"""

age = int(input("나이를 입력하세요: "))

# 나이 구간별로 구분과 요금을 정한다
if age <= 7:
    category = "무료"
    price = 0
elif age <= 13:
    category = "어린이"
    price = 5000
elif age <= 19:
    category = "청소년"
    price = 8000
elif age <= 64:
    category = "성인"
    price = 12000
else:
    category = "경로"
    price = 5000

print("나이: " + str(age) + "세")
print("구분: " + category)
print("요금: " + str(price) + "원")
