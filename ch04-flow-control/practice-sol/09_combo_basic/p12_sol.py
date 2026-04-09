"""
실습 12 풀이: 중고차 가격 산정
"""

new_price = int(input("신차 가격을 입력하세요 (만원): "))
year = int(input("연식을 입력하세요 (년): "))
km = float(input("주행거리를 입력하세요 (만 km): "))
accident = input("사고 유무를 입력하세요 (Y/N): ")

# 1) 연식 감가율 계산
if year <= 3:
    # 1~3년: 연당 10%
    year_discount = year * 10
elif year <= 7:
    # 4~7년: 처음 3년은 10%, 나머지는 7%
    year_discount = 3 * 10 + (year - 3) * 7
else:
    # 8년 이상: 처음 3년 10%, 다음 4년 7%, 나머지 5%
    year_discount = 3 * 10 + 4 * 7 + (year - 7) * 5

# 2) 주행거리 감가율
if km <= 5:
    km_discount = 0
elif km <= 10:
    km_discount = 5
else:
    km_discount = 10

# 3) 사고 감가율
if accident == "Y" or accident == "y":
    accident_discount = 15
else:
    accident_discount = 0

# 총 감가율 합산
total_discount = year_discount + km_discount + accident_discount

# 감가 내역 출력
print("--- 감가 내역 ---")
print("연식 감가 (" + str(year) + "년):", str(year_discount) + "%")
print("주행거리 감가:", str(km_discount) + "%")
print("사고 감가:", str(accident_discount) + "%")
print("총 감가율:", str(total_discount) + "%")

# 최종 가격 계산 (최소 신차 가격의 10%)
final_price = int(new_price * (1 - total_discount / 100))
min_price = int(new_price * 0.1)

if final_price < min_price:
    final_price = min_price

print("예상 중고차 가격:", str(final_price) + "만원")
