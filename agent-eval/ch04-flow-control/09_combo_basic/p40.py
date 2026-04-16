"""
TITLE: 문자 빈도
DIFFICULTY: medium
TAGS: nested-for, if, string

DESCRIPTION:
문자열을 입력받아 각 글자를 등장 순서대로 훑으며
해당 글자가 전체 문자열에서 몇 번 나오는지 이중 for문으로 세어
`문자: N개` 형태로 한 줄씩 출력하시오. (중복 출력 허용)

예시:
- 입력: `banana` → 출력: `b: 1개`, `a: 3개`, `n: 2개`, `a: 3개`, `n: 2개`, `a: 3개`
"""
# META_TESTS:
# - stdin: "banana"
#   expected_stdout: "b: 1개\na: 3개\nn: 2개\na: 3개\nn: 2개\na: 3개"
# - stdin: "abc"
#   expected_stdout: "a: 1개\nb: 1개\nc: 1개"

# 바깥 for는 선택, 안쪽 for는 개수 세기
text = input()
# TODO
