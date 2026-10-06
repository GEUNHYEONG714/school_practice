"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 70: 숫자 분해

3자리 정수를 입력받아 백의자리, 십의자리, 일의자리로 분해하고,
세 자리의 합과 곱을 출력합니다.

힌트: 나눗셈(//)과 나머지(%) 연산을 사용하여 각 자리를 분리합니다.
"""

num = int(input("3자리 정수를 입력하세요: "))

# 아래에 코드를 작성하세요
# 각 자리 분리
hundred = num // 100
ten = (num // 10) % 10
one = num % 10

# 합과 곱
total = hundred + ten + one
multiply = hundred * ten * one

# 출력
print(f"백의자리: {hundred}")
print(f"십의자리: {ten}")
print(f"일의자리: {one}")
print(f"합: {total}")
print(f"곱: {multiply}")

"""
[실행 결과 예시] (입력: 357)
백의자리: 3
십의자리: 5
일의자리: 7
합: 15
곱: 105
"""
