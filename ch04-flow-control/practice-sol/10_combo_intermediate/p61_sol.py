"""
실습 61 풀이: 최대 연속 합
"""

n = int(input("N을 입력하세요: "))
nums = input("정수들을 입력하세요: ")

parts = nums.split()
first = True
current_sum = 0
max_sum = 0

for p in parts:
    val = int(p)
    if first:
        current_sum = val
        max_sum = val
        first = False
    else:
        # 현재 값을 더하거나, 현재 값부터 새로 시작
        if current_sum + val > val:
            current_sum = current_sum + val
        else:
            current_sum = val
        # 최대값 갱신
        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)
