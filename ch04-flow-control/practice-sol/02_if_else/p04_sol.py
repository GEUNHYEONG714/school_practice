"""
실습 4 풀이: 배터리 잔량 확인
"""

battery = int(input("배터리 잔량(%)을 입력하세요: "))

# 20% 이하이면 충전 필요, 아니면 배터리 충분
if battery <= 20:
    print("충전 필요")
else:
    print("배터리 충분")
