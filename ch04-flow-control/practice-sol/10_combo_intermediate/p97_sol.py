"""
실습 97 풀이: 매직 스퀘어 검증
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

# 행 합
row0 = r0c0 + r0c1 + r0c2
row1 = r1c0 + r1c1 + r1c2
row2 = r2c0 + r2c1 + r2c2

# 열 합
col0 = r0c0 + r1c0 + r2c0
col1 = r0c1 + r1c1 + r2c1
col2 = r0c2 + r1c2 + r2c2

# 대각선 합
diag1 = r0c0 + r1c1 + r2c2  # 주대각선
diag2 = r0c2 + r1c1 + r2c0  # 부대각선

# 모두 같은지 확인
target = row0
if row1 == target and row2 == target and col0 == target and col1 == target and col2 == target and diag1 == target and diag2 == target:
    print("YES")
    print(target)
else:
    print("NO")
