"""
실습 94 풀이: 계산기 반복 (3회)
"""

total = 0

for i in range(3):
    line = input()
    parts = line.split()
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a // b

    print(result)
    total += result

print("합계:", total)
