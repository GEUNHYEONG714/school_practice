"""
실습 64 풀이: 숫자 카운트
"""

n = int(input("정수 N을 입력하세요: "))

count3 = 0
count5 = 0
count15 = 0

# 1부터 N까지 반복하며 배수 카운트
for i in range(1, n + 1):
    if i % 3 == 0:
        count3 += 1
    if i % 5 == 0:
        count5 += 1
    if i % 15 == 0:
        count15 += 1

print("3의 배수: " + str(count3) + "개")
print("5의 배수: " + str(count5) + "개")
print("3과 5의 공배수: " + str(count15) + "개")
