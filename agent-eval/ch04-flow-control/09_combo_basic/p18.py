"""
TITLE: 양수/음수/0 카운트
DIFFICULTY: medium
TAGS: for, if, elif, else, counter
EVAL: stdio

DESCRIPTION:
10개의 정수를 한 줄에 하나씩 입력받아 양수/음수/0의 개수를 세어 출력하시오.

출력 형식 (3줄):
`양수: X개`
`음수: X개`
`0: X개`

예시:
- 입력: `5\n-3\n0\n7\n-1\n2\n0\n-8\n4\n6` → 양수 5, 음수 3, 0 2
"""
# META_TESTS:
# - stdin: "5\n-3\n0\n7\n-1\n2\n0\n-8\n4\n6"
#   expected_stdout: "양수: 5개\n음수: 3개\n0: 2개"
# - stdin: "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
#   expected_stdout: "양수: 10개\n음수: 0개\n0: 0개"

# for + if/elif/else + 카운팅 변수를 사용하세요.
positive = 0
negative = 0
zero = 0
# TODO
