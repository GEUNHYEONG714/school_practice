"""
TITLE: X자 패턴
DIFFICULTY: hard
TAGS: pattern, nested_loop
EVAL: stdio

DESCRIPTION:
크기 n을 입력받아 N×N 격자에서 두 대각선 위치에만 별(`*`)을 출력하시오.
나머지 위치에는 공백을 출력합니다.
행 i, 열 j에서 `i == j` 또는 `i + j == n - 1`이면 대각선입니다.

예시:
- 입력: `3` → 출력: `* *\n * \n* *`
- 입력: `5` → 출력: `*   *\n * * \n  *  \n * * \n*   *`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "* *\n * \n* *"
# - stdin: "5"
#   expected_stdout: "*   *\n * * \n  *  \n * * \n*   *"
# - stdin: "1"
#   expected_stdout: "*"

# 행과 열을 순회하면서 대각선 조건을 확인하세요.
n = int(input())
# TODO
