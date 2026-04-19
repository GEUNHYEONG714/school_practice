"""
실습 54 풀이: 도서 대여료
"""

days = int(input("대여 일수를 입력하세요: "))

# 7일 초과분에 대해 일당 200원 부과
if days <= 7:
    fee = 0
else:
    fee = (days - 7) * 200

print("대여 일수: " + str(days) + "일")
print("대여료: " + str(fee) + "원")
