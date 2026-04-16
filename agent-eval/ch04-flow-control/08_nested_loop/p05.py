"""
TITLE: 직각삼각형 (오른쪽 정렬)
DIFFICULTY: medium
TAGS: nested-loop, for, pattern, stars

DESCRIPTION:
줄 수 N을 입력받아, 오른쪽으로 정렬된 별 삼각형을 출력하시오.
i번째 줄(1부터 시작)에는 공백 (N-i)개와 별 i개를 출력합니다.

예시:
- 입력: `3` → 출력: `  *\n **\n***`
- 입력: `5` → 출력: `    *\n   **\n  ***\n ****\n*****`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "  *\n **\n***"
# - stdin: "5"
#   expected_stdout: "    *\n   **\n  ***\n ****\n*****"
# - stdin: "1"
#   expected_stdout: "*"

# 공백을 먼저 (n-i)개 출력한 뒤 별을 i개 출력하세요.
n = int(input())
# TODO
