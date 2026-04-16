"""
TITLE: 숫자 자릿수 세기
DIFFICULTY: easy
TAGS: while, integer-division, digits

EVAL: stdio

DESCRIPTION:
양의 정수를 입력받아 몇 자리 수인지 `N은(는) C자리 수입니다.` 형식(f-string)으로 출력하시오.

예시:
- 입력: `12345` → 출력: `12345은(는) 5자리 수입니다.`
- 입력: `7` → 출력: `7은(는) 1자리 수입니다.`
"""
# META_TESTS:
# - stdin: "12345"
#   expected_stdout: "12345은(는) 5자리 수입니다."
# - stdin: "7"
#   expected_stdout: "7은(는) 1자리 수입니다."
# - stdin: "100"
#   expected_stdout: "100은(는) 3자리 수입니다."

# 원본 값을 따로 보관하고, while num > 0: num //= 10; count += 1 로 자릿수를 세세요.
num = int(input())
count = 0
# TODO
