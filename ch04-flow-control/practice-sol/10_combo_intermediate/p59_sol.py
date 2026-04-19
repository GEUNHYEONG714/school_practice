"""
실습 59 풀이: 소수 간격 찾기
"""

n = int(input("N을 입력하세요: "))

prime_str = ""      # 소수 목록 문자열
prev_prime = 0      # 이전 소수
max_gap = 0         # 최대 간격
gap_start = 0       # 최대 간격 시작 소수
gap_end = 0         # 최대 간격 끝 소수

for i in range(2, n + 1):
    # 소수 판별
    is_prime = True
    if i < 2:
        is_prime = False
    for j in range(2, i):
        if j * j > i:
            break
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        # 소수 목록 문자열에 추가
        if prime_str == "":
            prime_str = str(i)
        else:
            prime_str += " " + str(i)

        # 간격 비교
        if prev_prime > 0:
            gap = i - prev_prime
            if gap > max_gap:
                max_gap = gap
                gap_start = prev_prime
                gap_end = i

        prev_prime = i

print(f"소수 목록: {prime_str}")
print(f"최대 간격: {gap_start}과 {gap_end} 사이 (간격: {max_gap})")
