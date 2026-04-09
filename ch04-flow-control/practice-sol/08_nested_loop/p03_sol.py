"""
실습 3 풀이: 구구단 전체 출력
"""

# 바깥 for문: 단 (2단 ~ 9단)
for i in range(2, 10):
    print(f"--- {i}단 ---")
    # 안쪽 for문: 곱하는 수 (1 ~ 9)
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()  # 단 사이에 빈 줄
