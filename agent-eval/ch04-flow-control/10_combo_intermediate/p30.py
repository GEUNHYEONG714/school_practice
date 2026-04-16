"""
TITLE: 숫자 테두리 사각형
DIFFICULTY: hard
TAGS: pattern, nested_loop
EVAL: stdio

DESCRIPTION:
크기 n을 입력받아 N×N 사각형을 출력하시오.
각 위치 (i, j)에서 가장 가까운 테두리까지의 거리 + 1을 값으로 출력합니다.
(바깥 테두리는 1, 한 칸 안은 2, 그 다음은 3, ...)
숫자 사이에는 공백 하나를 둡니다.

예시:
- 입력: `3` → 출력: `1 1 1\n1 2 1\n1 1 1`
- 입력: `5` → 출력: `1 1 1 1 1\n1 2 2 2 1\n1 2 3 2 1\n1 2 2 2 1\n1 1 1 1 1`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "1 1 1\n1 2 1\n1 1 1"
# - stdin: "1"
#   expected_stdout: "1"
# - stdin: "5"
#   expected_stdout: "1 1 1 1 1\n1 2 2 2 1\n1 2 3 2 1\n1 2 2 2 1\n1 1 1 1 1"

# min(i, j, n-1-i, n-1-j) + 1로 계산하세요.
n = int(input())
# TODO
