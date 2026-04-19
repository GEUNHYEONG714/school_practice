"""
실습 62 풀이: 두 수의 곱 최대
"""

n = int(input("N을 입력하세요: "))
nums = input("정수들을 입력하세요: ")

parts = nums.split()
max_product = None

# 이중 for문으로 모든 쌍 비교
idx_i = 0
for p1 in parts:
    val1 = int(p1)
    idx_j = 0
    for p2 in parts:
        val2 = int(p2)
        if idx_i < idx_j:  # 서로 다른 위치
            product = val1 * val2
            if max_product is None or product > max_product:
                max_product = product
        idx_j += 1
    idx_i += 1

print(max_product)
