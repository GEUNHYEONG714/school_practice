"""
실습 풀이: 최소값 찾기
"""

# 첫 번째 숫자를 먼저 입력받아 최소값으로 설정
minimum = int(input("1번째 숫자: "))

# 나머지 4개의 숫자를 입력받으며 비교
for i in range(2, 6):
    num = int(input(str(i) + "번째 숫자: "))

    # 입력된 숫자가 현재 최소값보다 작으면 갱신
    if num < minimum:
        minimum = num

print("최소값:", minimum)
