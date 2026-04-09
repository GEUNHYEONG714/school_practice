"""
실습 풀이: 누적 합이 100 초과
"""

total = 0  # 누적합
count = 0  # 입력 횟수

# 누적합이 100을 넘을 때까지 반복
while True:
    num = int(input("숫자를 입력하세요: "))
    total += num  # 누적
    count += 1    # 횟수 증가

    # 누적합이 100을 초과하면 종료
    if total > 100:
        break

print("누적합이 100을 초과했습니다!")
print("누적합:", total)
print("입력 횟수:", count)
