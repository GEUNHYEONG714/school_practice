"""
TITLE: 1부터 N까지 합 (while)
DIFFICULTY: easy
TAGS: while, accumulator

EVAL: stdio

DESCRIPTION:
숫자 N을 입력받아 1부터 N까지의 합을 `1부터 N까지의 합: 합계` 형식(f-string)으로 출력하시오.

예시:
- 입력: `10` → 출력: `1부터 10까지의 합: 55`
- 입력: `100` → 출력: `1부터 100까지의 합: 5050`
"""
# META_TESTS:
# - stdin: "10"
#   expected_stdout: "1부터 10까지의 합: 55"
# - stdin: "1"
#   expected_stdout: "1부터 1까지의 합: 1"
# - stdin: "100"
#   expected_stdout: "1부터 100까지의 합: 5050"

# i = 1, while i <= n: total += i; i += 1
n = int(input())
total = 0
# TODO
