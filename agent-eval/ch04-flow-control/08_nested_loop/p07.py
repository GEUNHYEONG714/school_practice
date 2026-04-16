"""
TITLE: 알파벳 삼각형
DIFFICULTY: medium
TAGS: nested-loop, for, pattern, alphabet

DESCRIPTION:
줄 수 N을 입력받아, i번째 줄에 A부터 시작해 i개의 알파벳을 이어붙여 출력하시오.

예시:
- 입력: `3` → 출력: `A\nAB\nABC`
- 입력: `5` → 출력: `A\nAB\nABC\nABCD\nABCDE`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "A\nAB\nABC"
# - stdin: "5"
#   expected_stdout: "A\nAB\nABC\nABCD\nABCDE"
# - stdin: "1"
#   expected_stdout: "A"

# chr(65)는 'A', chr(65+1)은 'B'입니다.
n = int(input())
# TODO
