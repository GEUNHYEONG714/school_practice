"""
실습 56 풀이: 행복한 수
"""

num = int(input("양의 정수를 입력하세요: "))

original = num
current = num
step = 0
is_happy = False

while step < 100:
    # 자릿수 제곱합 구하기
    digit_sq_sum = 0
    temp = current
    while temp > 0:
        digit = temp % 10
        digit_sq_sum += digit ** 2
        temp //= 10

    step += 1
    print(f"단계 {step}: {current} → {digit_sq_sum}")

    if digit_sq_sum == 1:
        is_happy = True
        break

    # 시작값으로 되돌아오면 순환
    if digit_sq_sum == original:
        break

    current = digit_sq_sum

if is_happy:
    print(f"{original}은(는) 행복한 수입니다!")
else:
    print(f"{original}은(는) 행복한 수가 아닙니다.")
