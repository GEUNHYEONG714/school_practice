"""
실습 30 풀이: 수 분류기
"""

pos_sum = 0    # 양수의 합
neg_sum = 0    # 음수의 합
zero_count = 0  # 0의 개수

# 10개의 숫자를 입력받아 분류
for i in range(1, 11):
    num = int(input(str(i) + "번째 숫자: "))

    # 양수, 음수, 0으로 분류
    if num > 0:
        pos_sum += num
    elif num < 0:
        neg_sum += num
    else:
        zero_count += 1

print("양수의 합:", pos_sum)
print("음수의 합:", neg_sum)
print("0의 개수:", zero_count)
