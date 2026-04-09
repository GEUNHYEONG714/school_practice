"""
실습 5 풀이: 팩토리얼 합
"""

n = int(input("N을 입력하세요: "))

total = 0       # 팩토리얼 합계
factorial = 1   # 현재 팩토리얼 값

for i in range(1, n + 1):
    # 이전 팩토리얼에 i를 곱하면 i!이 됨 (효율적 방법)
    factorial *= i
    print(str(i) + "! = " + str(factorial))
    total += factorial

# 수식과 합계 출력
result_str = ""
for i in range(1, n + 1):
    if i == 1:
        result_str = "1!"
    else:
        result_str = result_str + " + " + str(i) + "!"

print(result_str + " = " + str(total))
