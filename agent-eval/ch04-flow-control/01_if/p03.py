"""
TITLE: 폭염 경보
DIFFICULTY: easy
TAGS: if, comparison, print
EVAL: stdio

DESCRIPTION:
온도를 입력받아 30도를 초과하면 아래 두 줄을 순서대로 출력하시오.
- `폭염주의보`
- `외출을 자제하세요`
30도 이하이면 아무것도 출력하지 마시오.

예시:
- 입력: `35` → 출력: `폭염주의보\n외출을 자제하세요`
- 입력: `25` → 출력: (없음)
- 입력: `30` → 출력: (없음)
"""
# META_TESTS:
# - stdin: "35"
#   expected_stdout: "폭염주의보\n외출을 자제하세요"
# - stdin: "25"
#   expected_stdout: ""
# - stdin: "30"
#   expected_stdout: ""

# 온도를 입력받아 30도 초과이면 두 줄을 출력하세요.
temperature = int(input())
# TODO
