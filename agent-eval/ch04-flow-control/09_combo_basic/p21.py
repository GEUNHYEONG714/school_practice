"""
TITLE: M의 배수 합계
DIFFICULTY: medium
TAGS: for, if, accumulator
EVAL: stdio

DESCRIPTION:
두 자연수 N과 M을 각각 한 줄씩 입력받아, 1부터 N까지 중 M의 배수의 합을 출력하시오.

출력 형식: `1부터 N까지 M의 배수의 합: 값`

예시:
- 입력: `20\n3` → 출력: `1부터 20까지 3의 배수의 합: 63`
"""
# META_TESTS:
# - stdin: "20\n3"
#   expected_stdout: "1부터 20까지 3의 배수의 합: 63"
# - stdin: "10\n2"
#   expected_stdout: "1부터 10까지 2의 배수의 합: 30"
# - stdin: "100\n5"
#   expected_stdout: "1부터 100까지 5의 배수의 합: 1050"

# for + if(i % m == 0) + 누적 변수를 사용하세요.
n = int(input())
m = int(input())
# TODO
