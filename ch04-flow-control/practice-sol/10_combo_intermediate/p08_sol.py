"""
실습 8 풀이: 진법 변환 (10진수 → 2진수)
"""

num = int(input("양의 정수를 입력하세요: "))

original_num = num  # 원래 값 저장
binary = ""         # 2진수 결과 문자열

# 0인 경우 별도 처리
if num == 0:
    binary = "0"
    print(str(original_num) + " → 2진수: " + binary)
else:
    print("변환 과정:")

    # 2로 나누기를 반복하여 2진수 구하기
    while num > 0:
        remainder = num % 2     # 나머지 (0 또는 1)
        quotient = num // 2     # 몫

        # 변환 과정 출력
        print("  " + str(num) + " ÷ 2 = " + str(quotient) + " ... 나머지 " + str(remainder))

        # 나머지를 결과 문자열 앞에 추가 (역순)
        binary = str(remainder) + binary
        num = quotient

    print(str(original_num) + " → 2진수: " + binary)
