"""
TITLE: 수열 패턴 찾기 (삼각수)
DIFFICULTY: hard
TAGS: algorithm, math, for, sequence
EVAL: stdio

DESCRIPTION:
양의 정수 N을 입력받아, 1번째부터 N번째까지의 삼각수를 출력하시오.

삼각수란 1부터 K까지의 합으로, K번째 삼각수 = 1+2+...+K 이다.
(1, 3, 6, 10, 15, 21, ...)

각 삼각수를 `T(K) = 값` 형식으로 한 줄에 하나씩 출력하고,
마지막에 빈 줄 없이 `합계: X` (모든 삼각수의 합)을 출력한다.

예시:
- 입력: `5` → T(1)=1, T(2)=3, T(3)=6, T(4)=10, T(5)=15, 합계=35
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "T(1) = 1\nT(2) = 3\nT(3) = 6\nT(4) = 10\nT(5) = 15\n합계: 35"
# - stdin: "1"
#   expected_stdout: "T(1) = 1\n합계: 1"
# - stdin: "7"
#   expected_stdout: "T(1) = 1\nT(2) = 3\nT(3) = 6\nT(4) = 10\nT(5) = 15\nT(6) = 21\nT(7) = 28\n합계: 84"

# 누적합으로 삼각수를 구하고, 전체 합도 함께 누적
n = int(input())
# TODO
