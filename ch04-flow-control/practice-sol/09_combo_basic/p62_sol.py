"""
실습 62 풀이: 영화관 좌석
"""

seat = int(input("좌석번호를 입력하세요: "))

# 범위 확인
if seat < 1 or seat > 100:
    print("잘못된 좌석번호입니다.")
else:
    # 열 번호 (0~9) → A~J
    row = chr(ord("A") + (seat - 1) // 10)
    # 좌석 번호 (1~10)
    num = (seat - 1) % 10 + 1
    print("좌석 " + str(seat) + " → " + row + "열 " + str(num) + "번")
