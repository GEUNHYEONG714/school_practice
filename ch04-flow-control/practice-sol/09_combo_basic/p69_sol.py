"""
실습 69 풀이: 가격표 출력
"""

price = int(input("단가를 입력하세요: "))
n = int(input("수량범위를 입력하세요: "))

# 1부터 N까지 가격표 출력
for i in range(1, n + 1):
    print(str(i) + " x " + str(price) + " = " + str(i * price))
