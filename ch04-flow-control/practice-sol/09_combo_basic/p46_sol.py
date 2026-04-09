"""
실습 46 풀이: 가계부
"""

balance = 0       # 현재 잔액
total_income = 0   # 총 수입
total_expense = 0  # 총 지출

print("=== 가계부 ===")
print("1.수입  2.지출  0.종료")

while True:
    choice = int(input("선택: "))

    # 종료 조건
    if choice == 0:
        break

    # 수입 처리
    if choice == 1:
        amount = int(input("금액: "))
        balance += amount
        total_income += amount
        print("[수입] +" + str(amount) + "원 | 잔액: " + str(balance) + "원")

    # 지출 처리
    elif choice == 2:
        amount = int(input("금액: "))
        balance -= amount
        total_expense += amount
        print("[지출] -" + str(amount) + "원 | 잔액: " + str(balance) + "원")

print("=== 종합 요약 ===")
print("총 수입:", total_income, "원")
print("총 지출:", total_expense, "원")
print("최종 잔액:", balance, "원")
