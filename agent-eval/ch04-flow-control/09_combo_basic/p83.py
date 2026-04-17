"""
TITLE: 소인수분해
DIFFICULTY: medium
TAGS: while, if, arithmetic, modulo
EVAL: stdio

DESCRIPTION:
정수를 입력받아 소인수분해 결과를 출력하시오.

출력 형식: 소인수들을 `x`로 연결하여 한 줄에 출력합니다.
(앞뒤 공백 포함: ` x `)

예시:
- 입력: `12` → 출력: `2 x 2 x 3`
- 입력: `7` → 출력: `7`
"""
# META_TESTS:
# - stdin: "12"
#   expected_stdout: "2 x 2 x 3"
# - stdin: "60"
#   expected_stdout: "2 x 2 x 3 x 5"
# - stdin: "7"
#   expected_stdout: "7"

# 정수를 소인수분해하여 결과를 출력하세요.
n = int(input())
# TODO
