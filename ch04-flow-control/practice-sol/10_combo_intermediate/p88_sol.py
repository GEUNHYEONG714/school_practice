"""
실습 88 풀이: 스도쿠 검증 (3x3)
"""
r0c0, r0c1, r0c2 = input().split()
r1c0, r1c1, r1c2 = input().split()
r2c0, r2c1, r2c2 = input().split()

# 정수 변환
r0c0 = int(r0c0)
r0c1 = int(r0c1)
r0c2 = int(r0c2)
r1c0 = int(r1c0)
r1c1 = int(r1c1)
r1c2 = int(r1c2)
r2c0 = int(r2c0)
r2c1 = int(r2c1)
r2c2 = int(r2c2)

# 격자 출력
print("--- 3x3 검증 ---")
print(str(r0c0) + " " + str(r0c1) + " " + str(r0c2))
print(str(r1c0) + " " + str(r1c1) + " " + str(r1c2))
print(str(r2c0) + " " + str(r2c1) + " " + str(r2c2))

# 1~9 각 숫자 존재 여부 플래그
has1 = (r0c0 == 1 or r0c1 == 1 or r0c2 == 1 or r1c0 == 1 or r1c1 == 1 or r1c2 == 1 or r2c0 == 1 or r2c1 == 1 or r2c2 == 1)
has2 = (r0c0 == 2 or r0c1 == 2 or r0c2 == 2 or r1c0 == 2 or r1c1 == 2 or r1c2 == 2 or r2c0 == 2 or r2c1 == 2 or r2c2 == 2)
has3 = (r0c0 == 3 or r0c1 == 3 or r0c2 == 3 or r1c0 == 3 or r1c1 == 3 or r1c2 == 3 or r2c0 == 3 or r2c1 == 3 or r2c2 == 3)
has4 = (r0c0 == 4 or r0c1 == 4 or r0c2 == 4 or r1c0 == 4 or r1c1 == 4 or r1c2 == 4 or r2c0 == 4 or r2c1 == 4 or r2c2 == 4)
has5 = (r0c0 == 5 or r0c1 == 5 or r0c2 == 5 or r1c0 == 5 or r1c1 == 5 or r1c2 == 5 or r2c0 == 5 or r2c1 == 5 or r2c2 == 5)
has6 = (r0c0 == 6 or r0c1 == 6 or r0c2 == 6 or r1c0 == 6 or r1c1 == 6 or r1c2 == 6 or r2c0 == 6 or r2c1 == 6 or r2c2 == 6)
has7 = (r0c0 == 7 or r0c1 == 7 or r0c2 == 7 or r1c0 == 7 or r1c1 == 7 or r1c2 == 7 or r2c0 == 7 or r2c1 == 7 or r2c2 == 7)
has8 = (r0c0 == 8 or r0c1 == 8 or r0c2 == 8 or r1c0 == 8 or r1c1 == 8 or r1c2 == 8 or r2c0 == 8 or r2c1 == 8 or r2c2 == 8)
has9 = (r0c0 == 9 or r0c1 == 9 or r0c2 == 9 or r1c0 == 9 or r1c1 == 9 or r1c2 == 9 or r2c0 == 9 or r2c1 == 9 or r2c2 == 9)

if has1 and has2 and has3 and has4 and has5 and has6 and has7 and has8 and has9:
    print("결과: 유효합니다!")
else:
    print("결과: 유효하지 않습니다!")
