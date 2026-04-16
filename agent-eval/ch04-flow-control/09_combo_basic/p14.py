"""
TITLE: 짝수 개수 세기
DIFFICULTY: medium
TAGS: for, if, counter
EVAL: stdio

DESCRIPTION:
자연수 N을 입력받아 1부터 N까지 짝수의 개수를 `1부터 N까지 짝수의 개수: 값` 형식으로 출력하시오.

예시:
- 입력: `10` → 출력: `1부터 10까지 짝수의 개수: 5`
"""
# META_TESTS:
# - stdin: "10"
#   expected_stdout: "1부터 10까지 짝수의 개수: 5"
# - stdin: "7"
#   expected_stdout: "1부터 7까지 짝수의 개수: 3"
# - stdin: "1"
#   expected_stdout: "1부터 1까지 짝수의 개수: 0"

# for + if + 카운팅 변수를 사용하세요.
n = int(input())
# TODO
