"""
TITLE: 구간별 인원 카운트
DIFFICULTY: medium
TAGS: for, if, elif, else, counter
EVAL: stdio

DESCRIPTION:
10명의 점수를 한 줄에 하나씩 입력받아 구간별 인원 수를 출력하시오.

구간:
- 90점 이상
- 80점 이상 90점 미만
- 70점 이상 80점 미만
- 70점 미만

출력 형식 (4줄):
`90점 이상: X명`
`80점 이상: X명`
`70점 이상: X명`
`70점 미만: X명`

예시:
- 입력: `95\n82\n76\n91\n88\n65\n73\n90\n84\n55` → 90이상 3, 80이상 3, 70이상 2, 70미만 2
"""
# META_TESTS:
# - stdin: "95\n82\n76\n91\n88\n65\n73\n90\n84\n55"
#   expected_stdout: "90점 이상: 3명\n80점 이상: 3명\n70점 이상: 2명\n70점 미만: 2명"
# - stdin: "100\n100\n100\n100\n100\n100\n100\n100\n100\n100"
#   expected_stdout: "90점 이상: 10명\n80점 이상: 0명\n70점 이상: 0명\n70점 미만: 0명"

# for + if/elif/else + 카운팅 변수를 사용하세요.
a_count = 0
b_count = 0
c_count = 0
d_count = 0
# TODO
