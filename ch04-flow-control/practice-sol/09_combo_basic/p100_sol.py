"""
실습 100 풀이: 미니 은행
"""

balance = int(input("초기 잔액: "))

for i in range(3):
    line = input()
    parts = line.split()
    action = parts[0]

    if action == "입금":
        amount = int(parts[1])
        balance += amount
        print("입금 완료: 잔액 " + str(balance) + "원")
    elif action == "출금":
        amount = int(parts[1])
        if balance >= amount:
            balance -= amount
            print("출금 완료: 잔액 " + str(balance) + "원")
        else:
            print("출금 실패: 잔액 부족")
    elif action == "조회":
        print("현재 잔액: " + str(balance) + "원")

print("최종 잔액: " + str(balance) + "원")
