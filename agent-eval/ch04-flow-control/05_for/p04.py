"""
TITLE: 1부터 N까지의 합
DIFFICULTY: easy
TAGS: for, range, accumulator

EVAL: stdio

DESCRIPTION:
숫자 N을 입력받아 1부터 N까지의 합을 구하여 `1부터 N 까지의 합: 합계` 형식으로 출력하시오.
(print(..., n, "까지의 합:", total) 사용 — 콤마 구분으로 공백이 들어갑니다)

예시:
- 입력: `10` → 출력: `1부터 10 까지의 합: 55`
- 입력: `100` → 출력: `1부터 100 까지의 합: 5050`
"""
# META_TESTS:
# - stdin: "10"
#   expected_stdout: "1부터 10 까지의 합: 55"
# - stdin: "1"
#   expected_stdout: "1부터 1 까지의 합: 1"
# - stdin: "100"
#   expected_stdout: "1부터 100 까지의 합: 5050"

# for + range(1, n+1)로 누적합을 구한 뒤, print("1부터", n, "까지의 합:", total)로 출력하세요.
n = int(input())
# TODO
