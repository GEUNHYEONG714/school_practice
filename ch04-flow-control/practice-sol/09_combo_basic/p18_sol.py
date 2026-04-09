"""
실습 풀이: 양수/음수 카운트
"""

positive = 0  # 양수 개수
negative = 0  # 음수 개수
zero = 0      # 0 개수

# 10개의 숫자를 입력받으며 분류
for i in range(1, 11):
    num = int(input(str(i) + "번째 숫자: "))

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("양수:", str(positive) + "개")
print("음수:", str(negative) + "개")
print("0:", str(zero) + "개")
