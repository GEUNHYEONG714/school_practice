"""
TITLE: 할인 적용
DIFFICULTY: easy
TAGS: nested, if, else, string

EVAL: stdio

DESCRIPTION:
회원 여부(`Y`/`N`)를 입력받습니다. 회원이면(`Y`) VIP 여부(`Y`/`N`)를 추가로 입력받아 결과를 출력하시오.

- 회원 `Y`:
  - VIP `Y`: `20% 할인 적용`
  - VIP `N`: `10% 할인 적용`
- 회원 `N`: `할인 없음`

예시:
- 입력: `Y\nY` → 출력: `20% 할인 적용`
- 입력: `Y\nN` → 출력: `10% 할인 적용`
- 입력: `N` → 출력: `할인 없음`
"""
# META_TESTS:
# - stdin: "Y\nY"
#   expected_stdout: "20% 할인 적용"
# - stdin: "Y\nN"
#   expected_stdout: "10% 할인 적용"
# - stdin: "N"
#   expected_stdout: "할인 없음"

# 회원일 때만 VIP 여부를 input()으로 추가로 받으세요.
is_member = input()
# TODO
