"""
실습 26 풀이: 파스칼 삼각형
"""

n = int(input("줄 수 입력: "))

for i in range(n):
    # 앞쪽 공백 출력 (가운데 정렬)
    for s in range(n - 1 - i):
        print(" ", end="")

    # 이항계수 계산 및 출력 (누적 곱 방식)
    val = 1  # C(i, 0) = 1
    for k in range(i + 1):
        if k > 0:
            print(" ", end="")
        print(val, end="")
        # 다음 이항계수: C(i, k+1) = C(i, k) * (i - k) / (k + 1)
        val = val * (i - k) // (k + 1)

    print()
