"""
실습 4 풀이: 음수 입력시 종료
"""

total = 0

# 무한 반복으로 숫자를 계속 입력받는다
while True:
    num = int(input("숫자를 입력하세요: "))

    # 음수가 입력되면 반복 종료
    if num < 0:
        break

    # 음수가 아니면 합계에 누적
    total += num

# 반복이 끝난 뒤 합계 출력
print("합계:", total)
