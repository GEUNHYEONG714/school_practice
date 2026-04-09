"""
실습 49 풀이: 로또 번호 생성기

seed를 변형하며 수식으로 6개 번호를 생성합니다.
중복 시 +1씩 더해서 피합니다.
"""

seed = int(input("시드 번호를 입력하세요 (아무 숫자): "))

# 번호 생성 (seed를 변형하며 % 45 + 1)
n1 = (seed * 7 + 3) % 45 + 1

n2 = (n1 * 13 + 11) % 45 + 1
# 중복 확인
if n2 == n1:
    n2 = n2 % 45 + 1

n3 = (n2 * 17 + 7) % 45 + 1
# 중복 확인
if n3 == n1 or n3 == n2:
    n3 = n3 % 45 + 1
if n3 == n1 or n3 == n2:
    n3 = n3 % 45 + 1

n4 = (n3 * 23 + 5) % 45 + 1
# 중복 확인
if n4 == n1 or n4 == n2 or n4 == n3:
    n4 = n4 % 45 + 1
if n4 == n1 or n4 == n2 or n4 == n3:
    n4 = n4 % 45 + 1

n5 = (n4 * 29 + 13) % 45 + 1
# 중복 확인
if n5 == n1 or n5 == n2 or n5 == n3 or n5 == n4:
    n5 = n5 % 45 + 1
if n5 == n1 or n5 == n2 or n5 == n3 or n5 == n4:
    n5 = n5 % 45 + 1

n6 = (n5 * 31 + 17) % 45 + 1
# 중복 확인
if n6 == n1 or n6 == n2 or n6 == n3 or n6 == n4 or n6 == n5:
    n6 = n6 % 45 + 1
if n6 == n1 or n6 == n2 or n6 == n3 or n6 == n4 or n6 == n5:
    n6 = n6 % 45 + 1

print("=== 로또 번호 ===")
print("번호 1:", n1)
print("번호 2:", n2)
print("번호 3:", n3)
print("번호 4:", n4)
print("번호 5:", n5)
print("번호 6:", n6)
print("행운을 빕니다!")
