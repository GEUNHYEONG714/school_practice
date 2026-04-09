"""
실습 14 풀이: 짝수 개수 세기
"""

n = int(input("N을 입력하세요: "))

count = 0  # 짝수 개수를 셀 변수

# 1부터 N까지 반복
for i in range(1, n + 1):
    # 2로 나눈 나머지가 0이면 짝수
    if i % 2 == 0:
        count += 1

print("1부터 " + str(n) + "까지 짝수의 개수:", count)
