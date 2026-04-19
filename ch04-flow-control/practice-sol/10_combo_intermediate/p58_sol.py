"""
실습 58 풀이: 디지털 근
"""

num = int(input("양의 정수를 입력하세요: "))

step = 0

while num >= 10:
    # 덧셈식 문자열 구성
    s = str(num)
    expression = "+".join(s)   # "9+8+7+5"

    # 자릿수 합 계산
    digit_sum = 0
    for ch in s:
        digit_sum += int(ch)

    step += 1
    print(f"단계 {step}: 자릿수 합 계산 {expression} → {digit_sum}")
    num = digit_sum

print(f"디지털 근: {num}")
