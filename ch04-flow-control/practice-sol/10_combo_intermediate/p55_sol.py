"""
실습 55 풀이: 수열 패턴 찾기 (삼각수)
"""

n = int(input("N을 입력하세요: "))

tri = 0       # 현재 삼각수
total = 0     # 모든 삼각수의 합

for k in range(1, n + 1):
    tri += k                       # K번째 삼각수 = 이전 + K
    print(f"T({k}) = {tri}")
    total += tri

print(f"합계: {total}")
