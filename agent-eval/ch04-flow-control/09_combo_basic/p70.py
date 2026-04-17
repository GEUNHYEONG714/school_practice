"""
TITLE: 숫자 분해
DIFFICULTY: easy
TAGS: arithmetic, if, print
EVAL: stdio

DESCRIPTION:
3자리 정수를 입력받아 백의자리, 십의자리, 일의자리로 분해하고,
세 자리의 합과 곱을 출력하시오.

출력 형식:
`백의자리: X`
`십의자리: X`
`일의자리: X`
`합: X`
`곱: X`

예시:
- 입력: `357` → 백의자리 3, 십의자리 5, 일의자리 7, 합 15, 곱 105
"""
# META_TESTS:
# - stdin: "357"
#   expected_stdout: "백의자리: 3\n십의자리: 5\n일의자리: 7\n합: 15\n곱: 105"
# - stdin: "100"
#   expected_stdout: "백의자리: 1\n십의자리: 0\n일의자리: 0\n합: 1\n곱: 0"
# - stdin: "999"
#   expected_stdout: "백의자리: 9\n십의자리: 9\n일의자리: 9\n합: 27\n곱: 729"

# 3자리 정수를 입력받아 각 자리를 분해하고 합, 곱을 출력하세요.
num = int(input())
# TODO
