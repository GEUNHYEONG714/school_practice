"""
TITLE: 배터리 잔량 확인
DIFFICULTY: easy
TAGS: if, else, comparison

EVAL: stdio

DESCRIPTION:
배터리 잔량(%)을 입력받아 20 이하이면 `충전 필요`, 아니면 `배터리 충분`을 출력하시오.

예시:
- 입력: `15` → 출력: `충전 필요`
- 입력: `80` → 출력: `배터리 충분`
- 입력: `20` → 출력: `충전 필요`
"""
# META_TESTS:
# - stdin: "15"
#   expected_stdout: "충전 필요"
# - stdin: "80"
#   expected_stdout: "배터리 충분"
# - stdin: "20"
#   expected_stdout: "충전 필요"

# <= 연산자와 if/else를 사용하세요.
battery = int(input())
# TODO
