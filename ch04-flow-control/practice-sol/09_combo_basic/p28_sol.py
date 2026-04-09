"""
실습 28 풀이: 완전수 판별
"""

num = int(input("숫자를 입력하세요: "))
total = 0  # 약수의 합

# 자기 자신을 제외한 약수의 합 구하기
for i in range(1, num):
    if num % i == 0:
        total += i

print(str(num) + "의 약수의 합:", total)

# 약수의 합이 자기 자신과 같으면 완전수
if total == num:
    print(str(num) + "은(는) 완전수입니다!")
else:
    print(str(num) + "은(는) 완전수가 아닙니다.")
