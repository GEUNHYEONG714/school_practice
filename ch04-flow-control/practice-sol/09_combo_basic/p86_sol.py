"""
실습 86 풀이: 콜라츠 추측
"""

n = int(input("정수를 입력하세요: "))

count = 0
# 시작 숫자 출력
print(n)

# 1이 될 때까지 반복
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    print(n)
    count += 1

print("횟수:", count)
