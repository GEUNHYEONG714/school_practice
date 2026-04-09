"""
실습 32 풀이: 온도 변환기
"""

print("1. 섭씨 → 화씨")
print("2. 화씨 → 섭씨")
mode = int(input("변환 모드를 선택하세요: "))
n = int(input("온도 개수를 입력하세요: "))

# 최고/최저 변환 온도 초기값
max_temp = -9999
min_temp = 9999

for i in range(n):
    temp = float(input("온도를 입력하세요: "))

    # 선택한 모드에 따라 변환
    if mode == 1:
        # 섭씨 → 화씨
        result = temp * 9 / 5 + 32
        print("변환 결과:", str(result) + "°F")
    elif mode == 2:
        # 화씨 → 섭씨
        result = (temp - 32) * 5 / 9
        print("변환 결과:", str(result) + "°C")

    # 최고/최저 온도 갱신
    if result > max_temp:
        max_temp = result
    if result < min_temp:
        min_temp = result

print("최고 변환 온도:", max_temp)
print("최저 변환 온도:", min_temp)
