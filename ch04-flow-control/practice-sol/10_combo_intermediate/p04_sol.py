"""
실습 4 풀이: 피보나치 수열
"""

n = int(input("N을 입력하세요: "))

print("피보나치 수열 (0~" + str(n) + "번째):")

# 첫 두 항 초기화
a = 0  # F(0)
b = 1  # F(1)

# 0번째부터 N번째까지 출력
for i in range(n + 1):
    if i == 0:
        print(a, end=" ")
    elif i == 1:
        print(b, end=" ")
    else:
        # 다음 항 = 이전 두 항의 합
        c = a + b
        a = b      # a를 한 칸 앞으로
        b = c      # b를 한 칸 앞으로
        print(b, end=" ")

print()  # 줄바꿈
