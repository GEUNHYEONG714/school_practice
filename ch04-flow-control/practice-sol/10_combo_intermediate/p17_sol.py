"""
실습 17 풀이: 증가수 찾기
"""

N = int(input("N을 입력하세요: "))

# 10부터 N까지 각 수에 대해 판별 (두 자리 이상)
num = 10
while num <= N:
    temp = num
    is_increasing = True
    # 오른쪽(일의 자리)부터 비교: 이전 자릿수보다 현재 자릿수가 작아야 함
    prev_digit = temp % 10  # 가장 오른쪽 자릿수
    temp //= 10

    while temp > 0:
        curr_digit = temp % 10  # 현재 자릿수 (왼쪽 방향)
        # 왼쪽 자릿수가 오른쪽 자릿수보다 크거나 같으면 증가수 아님
        if curr_digit >= prev_digit:
            is_increasing = False
            break
        prev_digit = curr_digit
        temp //= 10

    # 증가수이면 출력
    if is_increasing:
        print(num)

    num += 1
