"""
실습 9 풀이: 암스트롱 수 (Armstrong Number)
"""

print("3자리 암스트롱 수:")

# 100부터 999까지 모든 3자리 수를 검사
for num in range(100, 1000):
    # 각 자릿수 분리
    hundreds = num // 100          # 백의 자리
    tens = (num // 10) % 10        # 십의 자리
    ones = num % 10                # 일의 자리

    # 각 자릿수의 세제곱 합
    cube_sum = hundreds ** 3 + tens ** 3 + ones ** 3

    # 세제곱 합이 원래 수와 같으면 암스트롱 수
    if cube_sum == num:
        print(str(num) + " = " + str(hundreds) + "^3 + " + str(tens) + "^3 + " + str(ones) + "^3")
