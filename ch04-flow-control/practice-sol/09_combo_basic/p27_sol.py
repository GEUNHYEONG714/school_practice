"""
실습 27 풀이: 약수의 개수
"""

num = int(input("숫자를 입력하세요: "))
count = 0  # 약수 개수

# 1부터 입력한 숫자까지 반복
for i in range(1, num + 1):
    # 나누어 떨어지면 약수
    if num % i == 0:
        print(i)
        count += 1

print("약수의 개수:", count)
