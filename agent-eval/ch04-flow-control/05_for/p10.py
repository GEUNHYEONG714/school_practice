"""
TITLE: 누적 곱 계산
DIFFICULTY: easy
TAGS: for, range, input, accumulator

EVAL: stdio

DESCRIPTION:
첫 줄에 숫자의 개수 count를 입력받고, 그 다음 count개의 정수를 한 줄씩 입력받아
모든 숫자의 곱을 `누적 곱: 값` 형식으로 출력하시오.

예시:
- 입력: `3\n2\n3\n4` → 출력: `누적 곱: 24`
"""
# META_TESTS:
# - stdin: "3\n2\n3\n4"
#   expected_stdout: "누적 곱: 24"
# - stdin: "1\n7"
#   expected_stdout: "누적 곱: 7"
# - stdin: "4\n1\n2\n3\n5"
#   expected_stdout: "누적 곱: 30"

# 누적 곱 변수의 초깃값은 1로 두고, count번 반복하며 입력받은 숫자를 곱하세요.
count = int(input())
# TODO
