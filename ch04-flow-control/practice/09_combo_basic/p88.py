"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 88: 구간 소수

시작과 끝 정수를 입력받아 해당 구간의 소수만 출력하시오.

출력 형식: 소수를 한 줄에 공백으로 구분하여 출력합니다.

힌트: 각 숫자에 대해 2부터 해당 숫자-1까지 나누어 보며
      소수 여부를 판별합니다. 중첩 반복문을 사용하세요.
"""

start = int(input("시작 정수: "))
end = int(input("끝 정수: "))
# 아래에 코드를 작성하세요
prime_list = []

# 시작부터 끝까지 반복
for num in range(start, end + 1):

    # 소수 여부 플래그 선언
    is_prime = True

    # 2보다 작은 수는 소수가 아님
    if num < 2:
        is_prime = False

    # 2부터 num-1까지 나누기
    for div in range(2, num):

        # 나누어 떨어지면 소수가 아님
        if num % div == 0:
            is_prime = False
            break

    # 소수인 경우 리스트에 추가
    if is_prime:
        prime_list.append(num)

# 출력
print(*prime_list)
"""
[실행 결과 예시] (입력: 10, 20)
11 13 17 19

[실행 결과 예시] (입력: 1, 10)
2 3 5 7
"""
