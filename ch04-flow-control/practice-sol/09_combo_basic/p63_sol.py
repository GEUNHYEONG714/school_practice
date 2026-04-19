"""
실습 63 풀이: 구구단 범위 출력
"""

start = int(input("시작단을 입력하세요: "))
end = int(input("끝단을 입력하세요: "))

# 시작단부터 끝단까지 반복
for dan in range(start, end + 1):
    print("--- " + str(dan) + "단 ---")
    # 각 단의 1~9 곱셈
    for i in range(1, 10):
        print(str(dan) + " x " + str(i) + " = " + str(dan * i))
