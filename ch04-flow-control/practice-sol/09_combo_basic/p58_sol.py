"""
실습 58 풀이: 세금 계산기
"""

salary = int(input("연봉(만원)을 입력하세요: "))

# 누진세율로 구간별 세금 계산
tax = 0

if salary <= 1200:
    tax = int(salary * 0.06)
elif salary <= 4600:
    tax = int(1200 * 0.06) + int((salary - 1200) * 0.15)
else:
    tax = int(1200 * 0.06) + int((4600 - 1200) * 0.15) + int((salary - 4600) * 0.24)

print("연봉: " + str(salary) + "만원")
print("세금: " + str(tax) + "만원")
