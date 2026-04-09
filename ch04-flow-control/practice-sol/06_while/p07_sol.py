"""
실습 13 풀이: 최대값 찾기
"""

max_val = -1  # 최대값 초기화 (아직 없음)

num = int(input("숫자를 입력하세요 (-1=종료): "))

# -1이 아닌 동안 반복
while num != -1:
    # 현재 입력이 최대값보다 크면 갱신
    if num > max_val:
        max_val = num
    num = int(input("숫자를 입력하세요 (-1=종료): "))

# 최대값 출력 (-1만 입력한 경우 체크)
if max_val == -1:
    print("입력한 숫자가 없습니다.")
else:
    print(f"최대값: {max_val}")
