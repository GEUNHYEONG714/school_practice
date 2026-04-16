"""
TITLE: 사각형 테두리
DIFFICULTY: medium
TAGS: nested-loop, for, pattern, stars

DESCRIPTION:
크기 N을 입력받아, N x N 크기의 사각형 테두리를 `*`로 그리시오.
테두리가 아닌 안쪽은 공백(` `)으로 채웁니다.

예시:
- 입력: `3` → 출력: `***\n* *\n***`
- 입력: `5` → 출력: `*****\n*   *\n*   *\n*   *\n*****`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "***\n* *\n***"
# - stdin: "5"
#   expected_stdout: "*****\n*   *\n*   *\n*   *\n*****"
# - stdin: "2"
#   expected_stdout: "**\n**"

# i==0 또는 i==n-1 또는 j==0 또는 j==n-1 이면 테두리입니다.
n = int(input())
# TODO
