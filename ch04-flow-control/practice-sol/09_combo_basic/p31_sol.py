"""
실습 31 풀이: 구간 반복 합계
"""

start = int(input("시작값을 입력하세요: "))
end = int(input("끝값을 입력하세요: "))
total = 0     # 구간 합계
even_sum = 0  # 짝수 합계

# 시작값부터 끝값까지 반복
for i in range(start, end + 1):
    total += i

    # 짝수이면 짝수 합계에도 더하기
    if i % 2 == 0:
        even_sum += i

print("구간 합계:", total)
print("짝수 합계:", even_sum)
