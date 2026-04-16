"""
TITLE: 계절 판별
DIFFICULTY: easy
TAGS: if, elif, else, comparison

EVAL: stdio

DESCRIPTION:
월(1~12)을 입력받아 `{월}월은 {계절}입니다.` 형식으로 출력하시오.

계절 기준:
- 3, 4, 5월: 봄
- 6, 7, 8월: 여름
- 9, 10, 11월: 가을
- 12, 1, 2월: 겨울

예시:
- 입력: `7` → 출력: `7월은 여름입니다.`
- 입력: `12` → 출력: `12월은 겨울입니다.`
- 입력: `4` → 출력: `4월은 봄입니다.`
"""
# META_TESTS:
# - stdin: "7"
#   expected_stdout: "7월은 여름입니다."
# - stdin: "12"
#   expected_stdout: "12월은 겨울입니다."
# - stdin: "4"
#   expected_stdout: "4월은 봄입니다."

# 월을 계절로 변환하세요.
month = int(input())
# TODO
