"""
실습 29 풀이: 배수 찾기 게임 (FizzBuzz)
"""

for i in range(1, 51):
    # 공배수(15의 배수)를 먼저 검사해야 함
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
