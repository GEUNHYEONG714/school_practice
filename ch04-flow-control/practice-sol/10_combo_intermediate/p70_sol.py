"""
실습 70 풀이: 구간 최대값
"""

n, k = map(int, input("N K를 입력하세요: ").split())
nums = input("정수들을 입력하세요: ")

parts = nums.split()
result = ""

# 각 시작 위치 i에 대해 K개 구간의 최대값 구하기
for i in range(n - k + 1):
    max_val = None

    # i부터 K개 순회
    idx = 0
    for p in parts:
        val = int(p)
        if i <= idx < i + k:
            if max_val is None or val > max_val:
                max_val = val
        idx += 1

    if result == "":
        result = str(max_val)
    else:
        result += " " + str(max_val)

print(result)
