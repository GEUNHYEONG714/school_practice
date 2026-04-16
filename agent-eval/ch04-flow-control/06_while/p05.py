"""
TITLE: 숫자 뒤집기
DIFFICULTY: easy
TAGS: while, modulo, integer-division

EVAL: stdio

DESCRIPTION:
양의 정수를 입력받아 숫자를 뒤집어서 `뒤집은 숫자: 값` 형식(f-string)으로 출력하시오.
힌트: `digit = num % 10`, `reverse = reverse * 10 + digit`, `num //= 10`.

예시:
- 입력: `1234` → 출력: `뒤집은 숫자: 4321`
- 입력: `5678` → 출력: `뒤집은 숫자: 8765`
"""
# META_TESTS:
# - stdin: "1234"
#   expected_stdout: "뒤집은 숫자: 4321"
# - stdin: "5678"
#   expected_stdout: "뒤집은 숫자: 8765"
# - stdin: "7"
#   expected_stdout: "뒤집은 숫자: 7"

# while num > 0으로 반복하며 마지막 자리를 꺼내 reverse에 쌓으세요.
num = int(input())
reverse = 0
# TODO
