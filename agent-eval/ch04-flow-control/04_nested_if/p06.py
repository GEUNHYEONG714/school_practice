"""
TITLE: 놀이기구 탑승
DIFFICULTY: easy
TAGS: nested, if, else, comparison

EVAL: stdio

DESCRIPTION:
키(cm)를 입력받습니다. 키가 130cm 이상이면 보호자 동반 여부(`Y`/`N`)를 추가로 입력받아 판정하시오.

- 키 130cm 이상:
  - 보호자 `Y`: `보호자와 함께 탑승 가능합니다.`
  - 보호자 `N`:
    - 키 150cm 이상: `혼자 탑승 가능합니다.`
    - 키 150cm 미만: `보호자가 필요합니다.`
- 키 130cm 미만: `탑승할 수 없습니다.`

예시:
- 입력: `140\nY` → 출력: `보호자와 함께 탑승 가능합니다.`
- 입력: `140\nN` → 출력: `보호자가 필요합니다.`
- 입력: `155\nN` → 출력: `혼자 탑승 가능합니다.`
- 입력: `120` → 출력: `탑승할 수 없습니다.`
"""
# META_TESTS:
# - stdin: "140\nY"
#   expected_stdout: "보호자와 함께 탑승 가능합니다."
# - stdin: "140\nN"
#   expected_stdout: "보호자가 필요합니다."
# - stdin: "155\nN"
#   expected_stdout: "혼자 탑승 가능합니다."
# - stdin: "120"
#   expected_stdout: "탑승할 수 없습니다."

# 130cm 이상일 때만 보호자 입력을 받고, 그 안에서 다시 150cm 기준으로 나누세요.
height = int(input())
# TODO
