"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 66: 숫자 합 게임

첫 줄에 숫자 개수 N을 입력받고, 이어서 N개의 정수를 한 줄씩 입력받습니다.
양수의 합, 음수의 합, 전체 합을 각각 출력합니다.
(0은 양수/음수 어디에도 포함하지 않음)

힌트: for 반복문으로 N개의 숫자를 입력받으며 양수/음수를 구분합니다.
"""

n = int(input("숫자 개수를 입력하세요: "))

# 아래에 코드를 작성하세요
positive_sum = 0
negative_sum = 0

# N개의 숫자를 입력받음
for _ in range(n):
    num = int(input())

    # 양수인지 확인
    if num > 0:
        positive_sum += num

    # 음수인지 확인
    elif num < 0:
        negative_sum += num

# 전체 합 계산
total_sum = positive_sum + negative_sum

# 출력
print(f"양수 합: {positive_sum}")
print(f"음수 합: {negative_sum}")
print(f"전체 합: {total_sum}")

"""
[실행 결과 예시] (입력: 4, 3, -2, 5, -1)
양수 합: 8
음수 합: -3
전체 합: 5
"""
