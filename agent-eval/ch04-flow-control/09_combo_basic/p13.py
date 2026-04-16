"""
TITLE: 1~N 합계
DIFFICULTY: medium
TAGS: for, range, accumulator
EVAL: stdio

DESCRIPTION:
자연수 N을 입력받아 1부터 N까지의 합을 `1부터 N까지의 합: 값` 형식으로 출력하시오.

예시:
- 입력: `10` → 출력: `1부터 10까지의 합: 55`
"""
# META_TESTS:
# - stdin: "10"
#   expected_stdout: "1부터 10까지의 합: 55"
# - stdin: "100"
#   expected_stdout: "1부터 100까지의 합: 5050"
# - stdin: "1"
#   expected_stdout: "1부터 1까지의 합: 1"

# for + 누적 변수를 사용하세요.
n = int(input())
# TODO
