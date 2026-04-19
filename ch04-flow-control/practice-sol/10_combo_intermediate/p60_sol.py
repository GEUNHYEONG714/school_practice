"""
실습 60 풀이: 자기 기술 수열 (Look-and-Say)
"""

n = int(input("N을 입력하세요: "))

current = "1"

for i in range(1, n + 1):
    print(current)

    if i == n:
        break

    # 다음 항 구성
    next_seq = ""
    j = 0
    while j < len(current):
        ch = current[j]
        count = 1
        # 연속 같은 문자 세기
        while j + count < len(current) and current[j + count] == ch:
            count += 1
        next_seq += str(count) + ch
        j += count

    current = next_seq
