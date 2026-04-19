"""
실습 65 풀이: 물통 채우기
"""

c, n = map(int, input("용량 C와 물 개수 N을 입력하세요: ").split())

current = 0
overflowed = False

for i in range(1, n + 1):
    water = int(input("물의 양: "))
    current += water

    if current > c:
        overflow = current - c
        print(f"{i}번째에서 넘침! 넘친 양: {overflow}")
        overflowed = True
        break

if not overflowed:
    print("안 넘침")
