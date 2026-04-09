"""
실습 8 풀이: 1부터 N까지 합
"""

n = int(input("숫자를 입력하세요: "))

total = 0
i = 1

# i가 n 이하인 동안 반복
while i <= n:
    total += i  # total = total + i와 같다
    i += 1      # 다음 숫자로 이동

print(f"1부터 {n}까지의 합: {total}")
