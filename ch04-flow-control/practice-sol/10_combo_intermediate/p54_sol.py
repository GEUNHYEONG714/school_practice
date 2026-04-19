"""
실습 54 풀이: 디오판토스 방정식
"""

a, b, c = map(int, input("a b c를 입력하세요: ").split())

found = False
for x in range(101):
    remainder = c - a * x
    # b로 나누어 떨어지고 y가 0~100 범위인지 확인
    if b != 0 and remainder % b == 0:
        y = remainder // b
        if 0 <= y <= 100:
            print(f"x={x}, y={y}")
            found = True

if not found:
    print("해가 없습니다")
