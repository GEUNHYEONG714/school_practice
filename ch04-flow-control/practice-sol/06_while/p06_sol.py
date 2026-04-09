"""
실습 6 풀이: 평균 구하기
"""

total = 0
count = 0

num = int(input("숫자를 입력하세요 (0=종료): "))

# 0이 아닌 동안 반복
while num != 0:
    total += num  # 합계에 누적
    count += 1    # 개수 증가
    num = int(input("숫자를 입력하세요 (0=종료): "))

# 입력된 숫자가 있을 때만 평균 출력
if count > 0:
    print(f"평균: {total / count}")
else:
    print("입력한 숫자가 없습니다.")
