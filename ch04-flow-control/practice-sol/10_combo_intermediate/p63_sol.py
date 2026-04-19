"""
실습 63 풀이: 가장 긴 증가 구간
"""

n = int(input("N을 입력하세요: "))
nums = input("정수들을 입력하세요: ")

parts = nums.split()
max_len = 1
cur_len = 1
prev = None

for p in parts:
    val = int(p)
    if prev is not None:
        if val > prev:
            cur_len += 1
        else:
            cur_len = 1
        if cur_len > max_len:
            max_len = cur_len
    prev = val

print(max_len)
