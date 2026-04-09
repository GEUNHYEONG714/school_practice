"""
실습 5 풀이: 별 찍기
"""

n = int(input("줄 수를 입력하세요: "))

# 바깥 for문: 줄 수를 제어 (1줄, 2줄, 3줄, ...)
for i in range(1, n + 1):
    # 안쪽 for문: 해당 줄에 별을 i개 출력
    # end=""를 쓰면 줄바꿈 없이 옆으로 이어서 출력된다
    for j in range(i):
        print("*", end="")
    # 한 줄의 별을 다 찍은 후 줄바꿈
    print()
