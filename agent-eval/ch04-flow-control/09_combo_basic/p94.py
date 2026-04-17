"""
TITLE: 계산기 반복 (3회)
DIFFICULTY: medium
TAGS: for, if, elif, combo
EVAL: stdio

DESCRIPTION:
3번의 연산을 수행하는 계산기입니다.

각 연산마다 한 줄에 `숫자1 연산자 숫자2` 형태로 입력받습니다.
연산자는 +, -, *, / 중 하나입니다.
/ 연산은 정수 나눗셈(//)을 수행합니다.

3번의 연산 결과를 각각 한 줄씩 출력하고,
마지막 줄에 `합계: X`를 출력하시오. (X는 3번의 결과를 모두 더한 값)

예시:
- 입력: `10 + 5`, `20 - 3`, `4 * 6`
  → 출력: `15`, `17`, `24`, `합계: 56`
"""
# META_TESTS:
# - stdin: "10 + 5\n20 - 3\n4 * 6"
#   expected_stdout: "15\n17\n24\n합계: 56"
# - stdin: "100 / 3\n7 * 8\n50 - 25"
#   expected_stdout: "33\n56\n25\n합계: 114"
# - stdin: "1 + 1\n2 + 2\n3 + 3"
#   expected_stdout: "2\n4\n6\n합계: 12"

# 3번 반복하며 계산 결과를 누적하세요.
total = 0
# TODO
