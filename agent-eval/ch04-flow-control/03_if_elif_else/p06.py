"""
TITLE: 요일 판별
DIFFICULTY: easy
TAGS: if, elif, else, comparison

EVAL: stdio

DESCRIPTION:
숫자(1~7)를 입력받아 요일을 `{숫자} → {요일}` 형식으로 출력하시오.
1: 월요일, 2: 화요일, 3: 수요일, 4: 목요일, 5: 금요일, 6: 토요일, 7: 일요일.
1~7 범위를 벗어나면 `잘못된 입력입니다.`만 출력하시오.

예시:
- 입력: `3` → 출력: `3 → 수요일`
- 입력: `7` → 출력: `7 → 일요일`
- 입력: `9` → 출력: `잘못된 입력입니다.`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "3 → 수요일"
# - stdin: "7"
#   expected_stdout: "7 → 일요일"
# - stdin: "9"
#   expected_stdout: "잘못된 입력입니다."

# 1~7 외의 입력은 else로 처리하세요.
day = int(input())
# TODO
