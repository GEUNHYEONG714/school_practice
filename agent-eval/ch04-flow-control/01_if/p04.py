"""
TITLE: 우산 챙기기
DIFFICULTY: easy
TAGS: if, boolean, print
EVAL: stdio

DESCRIPTION:
비가 오는지 여부를 `True` 또는 `False`로 입력받아,
비가 오면 `우산을 챙기세요`를 출력하시오.
비가 오지 않으면 아무것도 출력하지 마시오.

힌트: 불리언 변수는 if 조건에 바로 넣을 수 있습니다.

예시:
- 입력: `True` → 출력: `우산을 챙기세요`
- 입력: `False` → 출력: (없음)
"""
# META_TESTS:
# - stdin: "True"
#   expected_stdout: "우산을 챙기세요"
# - stdin: "False"
#   expected_stdout: ""

# 비가 오면 "우산을 챙기세요"를 출력하세요.
is_raining = input() == "True"
# TODO
