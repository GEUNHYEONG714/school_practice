"""
TITLE: 나선형 숫자
DIFFICULTY: hard
TAGS: pattern, simulation, nested_loop
EVAL: stdio

DESCRIPTION:
크기 n을 입력받아 N×N 격자에 1부터 시작하여 시계 방향 나선형으로 숫자를 채워 출력하시오.
리스트를 사용하지 않고, 각 (r, c) 위치의 값을 층(layer) 계산으로 직접 구합니다.

출력 규칙:
- 숫자 사이에 공백 하나
- 숫자는 `len(str(n*n))` 자릿수로 오른쪽 정렬

예시:
- 입력: `3` → 출력: `1 2 3\n8 9 4\n7 6 5`
- 입력: `1` → 출력: `1`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "1 2 3\n8 9 4\n7 6 5"
# - stdin: "1"
#   expected_stdout: "1"
# - stdin: "4"
#   expected_stdout: " 1  2  3  4\n12 13 14  5\n11 16 15  6\n10  9  8  7"

# 각 위치의 층(layer)을 구해 이전까지의 칸 수와 층 내 위치로 값을 계산하세요.
n = int(input())
# TODO
