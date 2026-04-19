"""
실습 53 풀이: 수 뒤집어 더하기
"""

num = int(input("양의 정수를 입력하세요: "))

# 이미 회문인지 확인
if str(num) == str(num)[::-1]:
    print(f"이미 회문입니다: {num}")
else:
    step = 0
    while True:
        reversed_num = int(str(num)[::-1])
        total = num + reversed_num
        step += 1
        print(f"단계 {step}: {num} + {reversed_num} = {total}")

        # 합이 회문이면 종료
        if str(total) == str(total)[::-1]:
            print(f"회문 완성: {total} ({step}단계)")
            break

        num = total
