"""
TITLE: 홀짝 판별기
DIFFICULTY: easy
TAGS: if, else, modulo, comparison

EVAL: stdio

DESCRIPTION:
숫자를 입력받아 홀수인지 짝수인지 `{n}은(는) 홀수입니다` 또는 `{n}은(는) 짝수입니다` 형식으로 출력하시오.

예시:
- 입력: `7` → 출력: `7은(는) 홀수입니다`
- 입력: `4` → 출력: `4은(는) 짝수입니다`
- 입력: `0` → 출력: `0은(는) 짝수입니다`
"""
# META_TESTS:
# - stdin: "7"
#   expected_stdout: "7은(는) 홀수입니다"
# - stdin: "4"
#   expected_stdout: "4은(는) 짝수입니다"
# - stdin: "0"
#   expected_stdout: "0은(는) 짝수입니다"

# %(나머지) 연산자와 if/else를 사용해 홀짝을 판별하세요.
num = int(input())
# TODO
