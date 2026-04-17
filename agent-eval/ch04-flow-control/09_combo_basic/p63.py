"""
TITLE: 구구단 범위 출력
DIFFICULTY: easy
TAGS: for, nested-loop, range, print
EVAL: stdio

DESCRIPTION:
시작단과 끝단을 입력받아 해당 범위의 구구단을 출력하시오.

각 단은 `--- N단 ---`으로 시작하고,
`N x M = 결과` 형식으로 1~9까지 출력합니다.

예시:
- 입력: `2\n3` → 2단~3단 출력
"""
# META_TESTS:
# - stdin: "2\n3"
#   expected_stdout: "--- 2단 ---\n2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n--- 3단 ---\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27"
# - stdin: "5\n5"
#   expected_stdout: "--- 5단 ---\n5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45"
# - stdin: "8\n9"
#   expected_stdout: "--- 8단 ---\n8 x 1 = 8\n8 x 2 = 16\n8 x 3 = 24\n8 x 4 = 32\n8 x 5 = 40\n8 x 6 = 48\n8 x 7 = 56\n8 x 8 = 64\n8 x 9 = 72\n--- 9단 ---\n9 x 1 = 9\n9 x 2 = 18\n9 x 3 = 27\n9 x 4 = 36\n9 x 5 = 45\n9 x 6 = 54\n9 x 7 = 63\n9 x 8 = 72\n9 x 9 = 81"

# 시작단과 끝단을 입력받아 해당 범위의 구구단을 출력하세요.
start = int(input())
end = int(input())
# TODO
