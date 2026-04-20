"""
TITLE: 소인수분해
DIFFICULTY: medium
TAGS: while, if, arithmetic, modulo
EVAL: stdio

DESCRIPTION:
정수를 입력받아 소인수분해 결과를 출력하시오.

출력 형식:
- 소인수가 2개 이상이면 구분자 ` x ` (앞뒤 공백 포함)로 연결합니다.
- 소인수가 1개뿐이면(입력값 자체가 소수인 경우) 숫자만 출력합니다 (구분자 없음).
- 즉, 일반적인 문자열 join처럼 동작: ` x `.join(소인수들).

예시:
- 입력: `12` → 소인수 [2, 2, 3] → 출력: `2 x 2 x 3`
- 입력: `60` → 소인수 [2, 2, 3, 5] → 출력: `2 x 2 x 3 x 5`
- 입력: `7` → 소인수 [7] → 출력: `7` (구분자 없음)
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
