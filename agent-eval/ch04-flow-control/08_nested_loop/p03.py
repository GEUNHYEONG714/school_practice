"""
TITLE: 구구단 일부 출력
DIFFICULTY: medium
TAGS: nested-loop, for, multiplication

DESCRIPTION:
시작 단 `a`와 끝 단 `b`를 입력받아, a단부터 b단까지의 구구단을 출력하시오.
각 단의 시작에 `--- N단 ---`을 출력하고, 이어서 `N x 1 = N` 형식으로 1~9까지 출력합니다.
각 단이 끝나면 빈 줄을 한 줄 출력합니다.

예시:
- 입력: `2 2` → 2단 전체 출력
"""
# META_TESTS:
# - stdin: "2 2"
#   expected_stdout: "--- 2단 ---\n2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n"
# - stdin: "3 3"
#   expected_stdout: "--- 3단 ---\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n"

# 바깥 for문은 단, 안쪽 for문은 곱하는 수(1~9)입니다.
a, b = map(int, input().split())
# TODO
