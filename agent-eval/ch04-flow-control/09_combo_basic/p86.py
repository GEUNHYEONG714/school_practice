"""
TITLE: 콜라츠 추측
DIFFICULTY: medium
TAGS: while, if, else, arithmetic, counter
EVAL: stdio

DESCRIPTION:
정수를 입력받아 콜라츠 추측 과정을 출력하시오.

규칙:
- 짝수이면 2로 나눈다
- 홀수이면 3을 곱하고 1을 더한다
- 1이 될 때까지 반복한다

출력 형식:
- 각 단계의 숫자를 한 줄씩 출력 (시작 숫자 포함)
- 마지막 줄에 `횟수: N` 출력 (1이 되기까지의 단계 수)

예시:
- 입력: `6` → 6, 3, 10, 5, 16, 8, 4, 2, 1 → 횟수: 8
"""
# META_TESTS:
# - stdin: "6"
#   expected_stdout: "6\n3\n10\n5\n16\n8\n4\n2\n1\n횟수: 8"
# - stdin: "1"
#   expected_stdout: "1\n횟수: 0"
# - stdin: "3"
#   expected_stdout: "3\n10\n5\n16\n8\n4\n2\n1\n횟수: 7"

# 콜라츠 추측 과정과 횟수를 출력하세요.
n = int(input())
# TODO
