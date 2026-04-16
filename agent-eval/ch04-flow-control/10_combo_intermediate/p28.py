"""
TITLE: 체스판 패턴
DIFFICULTY: hard
TAGS: pattern, nested_loop
EVAL: stdio

DESCRIPTION:
크기 n을 입력받아 N×N 체스판을 출력하시오.
`#`과 `.`을 번갈아 출력하며, 행과 열의 합이 짝수이면 `#`, 홀수이면 `.`을 출력합니다.
각 문자 사이에는 공백 하나를 둡니다.

예시:
- 입력: `3` → 출력: `# . #\n. # .\n# . #`
- 입력: `1` → 출력: `#`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "# . #\n. # .\n# . #"
# - stdin: "1"
#   expected_stdout: "#"
# - stdin: "4"
#   expected_stdout: "# . # .\n. # . #\n# . # .\n. # . #"

# (i + j) % 2로 판정하세요.
n = int(input())
# TODO
