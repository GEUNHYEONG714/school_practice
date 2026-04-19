"""
실습 98 풀이: 타일 채우기
"""
n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    prev2 = 1  # f(1)
    prev1 = 2  # f(2)
    i = 3
    while i <= n:
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        i += 1
    print(prev1)
