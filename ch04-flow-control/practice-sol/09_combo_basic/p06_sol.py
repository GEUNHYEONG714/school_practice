"""
실습 6 풀이: 전기 요금 계산
"""

usage = int(input("전기 사용량을 입력하세요 (kWh): "))

# 누진제 구간별 요금 계산
if usage <= 100:
    # 100kWh 이하: 전부 60원
    charge = usage * 60
elif usage <= 200:
    # 101~200kWh: 처음 100은 60원, 나머지는 120원
    charge = 100 * 60 + (usage - 100) * 120
else:
    # 200kWh 초과: 60원 + 120원 + 190원 구간
    charge = 100 * 60 + 100 * 120 + (usage - 200) * 190

print("전기 요금:", str(charge) + "원")

# 부가세 10% 추가
tax = int(charge * 0.1)
print("부가세 (10%):", str(tax) + "원")

# 총 납부 금액
total = charge + tax
print("총 납부 금액:", str(total) + "원")
