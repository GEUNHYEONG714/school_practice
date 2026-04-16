"""
TITLE: 역 숫자 피라미드
DIFFICULTY: medium
TAGS: nested-loop, for, pattern, numbers

DESCRIPTION:
줄 수 N을 입력받아, 첫 줄에 N부터 1까지를 이어붙이고, 마지막 줄에는 1만 남는
역 숫자 피라미드를 출력하시오.

예시:
- 입력: `3` → 출력: `321\n21\n1`
- 입력: `5` → 출력: `54321\n4321\n321\n21\n1`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "321\n21\n1"
# - stdin: "5"
#   expected_stdout: "54321\n4321\n321\n21\n1"
# - stdin: "1"
#   expected_stdout: "1"

# range(i, 0, -1)로 i부터 1까지 역순 출력하세요.
n = int(input())
# TODO
