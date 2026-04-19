"""
실습 93 풀이: 비밀번호 생성기
"""

n = int(input("비밀번호 길이: "))

result = ""
alpha_idx = 0  # 알파벳 인덱스 (0=a, 1=b, ...)
num_idx = 1    # 숫자 (1부터 시작)

for i in range(n):
    if i % 2 == 0:
        # 홀수 번째 자리: 알파벳
        result += chr(ord('a') + alpha_idx % 26)
        alpha_idx += 1
    else:
        # 짝수 번째 자리: 숫자
        result += str(num_idx % 10)
        num_idx += 1

print(result)
