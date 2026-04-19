"""
실습 88 풀이: 구간 소수
"""

start = int(input("시작 정수: "))
end = int(input("끝 정수: "))

result = ""

for num in range(start, end + 1):
    if num < 2:
        continue

    # 소수 판별
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        if result != "":
            result += " "
        result += str(num)

print(result)
