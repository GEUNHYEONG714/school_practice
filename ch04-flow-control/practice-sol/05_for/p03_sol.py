"""
실습 11 풀이: 약수 구하기
"""

n = int(input("숫자를 입력하세요: "))

# end=" "로 줄바꿈 없이 한 줄에 이어서 출력
print(str(n) + "의 약수:", end=" ")

# 1부터 n까지 모든 수로 나눠본다
for i in range(1, n + 1):
    # n을 i로 나눈 나머지가 0이면 → i는 n의 약수
    if n % i == 0:
        print(i, end=" ")

print()  # 마지막 줄바꿈
