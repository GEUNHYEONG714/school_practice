"""
TITLE: 소수 판별
DIFFICULTY: hard
TAGS: algorithm, math, prime, while
EVAL: stdio

DESCRIPTION:
2 이상의 정수를 입력받아 소수인지 판별하세요.
소수이면 `N은(는) 소수입니다.`, 아니면 `N은(는) 소수가 아닙니다.`를 출력합니다.
(N은 입력값으로 치환됩니다)

예시:
- 입력: `7` → 출력: `7은(는) 소수입니다.`
- 입력: `12` → 출력: `12은(는) 소수가 아닙니다.`
- 입력: `2` → 출력: `2은(는) 소수입니다.`
"""
# META_TESTS:
# - stdin: "7"
#   expected_stdout: "7은(는) 소수입니다."
# - stdin: "12"
#   expected_stdout: "12은(는) 소수가 아닙니다."
# - stdin: "2"
#   expected_stdout: "2은(는) 소수입니다."

# 2 이상의 정수를 입력받아 소수 여부를 판별하세요.
num = int(input())
# TODO
