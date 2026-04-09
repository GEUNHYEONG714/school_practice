"""
실습 8 풀이: 동전 모으기
"""

goal = int(input("목표 금액을 입력하세요: "))

saved = 0

# 누적 금액이 목표 금액 미만인 동안 반복
while saved < goal:
    print(f"현재: {saved}원 / 목표: {goal}원")
    coin = int(input("동전 투입: "))
    saved += coin  # 누적 금액에 추가

# 목표 달성 출력
print(f"현재: {saved}원 / 목표: {goal}원")
print(f"목표 달성! 총 {saved}원을 모았습니다.")
