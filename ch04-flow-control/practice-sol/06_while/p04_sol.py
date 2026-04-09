"""
실습 4 풀이: 숫자 자릿수 세기
"""

num = int(input("양의 정수를 입력하세요: "))

original = num  # 출력용으로 원래 값 저장
count = 0

# num이 0보다 큰 동안 반복
while num > 0:
    num //= 10  # 10으로 나눠서 마지막 자리 제거
    count += 1  # 자릿수 1 증가

print(f"{original}은(는) {count}자리 수입니다.")
