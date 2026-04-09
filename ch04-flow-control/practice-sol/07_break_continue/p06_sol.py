"""
실습 13 풀이: 짝수만 누적
"""

total = 0

# 5번 반복하여 숫자를 입력받는다
for i in range(5):
    num = int(input("숫자를 입력하세요: "))

    # 홀수이면 건너뛴다
    if num % 2 != 0:
        print("홀수는 건너뜁니다")
        continue  # 아래 누적 코드를 건너뛰고 다음 반복으로

    # 짝수만 합계에 누적
    total += num

# 반복이 끝난 뒤 짝수 합계 출력
print("짝수 합계:", total)
