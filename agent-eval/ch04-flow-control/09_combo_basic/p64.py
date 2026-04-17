"""
TITLE: 숫자 카운트
DIFFICULTY: easy
TAGS: for, if, modulo, counter
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 1부터 N까지의 숫자 중에서:
- 3의 배수 개수
- 5의 배수 개수
- 3과 5 둘 다의 배수(15의 배수) 개수
를 각각 출력하시오.

출력 형식:
`3의 배수: X개`
`5의 배수: X개`
`3과 5의 공배수: X개`

예시:
- 입력: `15` → 3의 배수 5개, 5의 배수 3개, 공배수 1개
"""
# META_TESTS:
# - stdin: "15"
#   expected_stdout: "3의 배수: 5개\n5의 배수: 3개\n3과 5의 공배수: 1개"
# - stdin: "10"
#   expected_stdout: "3의 배수: 3개\n5의 배수: 2개\n3과 5의 공배수: 0개"
# - stdin: "30"
#   expected_stdout: "3의 배수: 10개\n5의 배수: 6개\n3과 5의 공배수: 2개"

# N을 입력받아 1~N에서 3의 배수, 5의 배수, 공배수 개수를 세어 출력하세요.
n = int(input())
# TODO
