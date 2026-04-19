"""
실습 66 풀이: 숫자 합 게임
"""

n = int(input("숫자 개수를 입력하세요: "))

pos_sum = 0
neg_sum = 0

# N개의 숫자를 입력받아 양수/음수 분류
for i in range(n):
    num = int(input("숫자를 입력하세요: "))
    if num > 0:
        pos_sum += num
    elif num < 0:
        neg_sum += num

print("양수 합: " + str(pos_sum))
print("음수 합: " + str(neg_sum))
print("전체 합: " + str(pos_sum + neg_sum))
