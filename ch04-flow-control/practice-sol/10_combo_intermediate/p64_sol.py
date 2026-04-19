"""
실습 64 풀이: 균형점 찾기
"""

n = int(input("N을 입력하세요: "))
nums = input("정수들을 입력하세요: ")

parts = nums.split()

# 전체 합 구하기
total = 0
for p in parts:
    total += int(p)

# 왼쪽 합을 누적하며 균형점 찾기
left_sum = 0
found = -1
idx = 0

for p in parts:
    val = int(p)
    right_sum = total - left_sum - val

    if left_sum == right_sum:
        found = idx
        break

    left_sum += val
    idx += 1

print(found)
