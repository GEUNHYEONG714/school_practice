"""
TITLE: 별 등급 표시
DIFFICULTY: medium
TAGS: for, if, elif, else
EVAL: stdio

DESCRIPTION:
먼저 학생 수 N을 입력받고, 이어서 N명의 점수를 한 줄에 하나씩 입력받습니다.
각 학생에 대해 점수에 따라 별(★)로 등급을 한 줄씩 출력하시오.

- 90점 이상: ★★★★★
- 80점 이상: ★★★★
- 70점 이상: ★★★
- 60점 이상: ★★
- 60점 미만: ★

출력 형식 (학생별 한 줄): `i번 학생: 별문자열`

예시:
- 입력: `3\n95\n73\n45` → 출력: `1번 학생: ★★★★★\n2번 학생: ★★★\n3번 학생: ★`
"""
# META_TESTS:
# - stdin: "3\n95\n73\n45"
#   expected_stdout: "1번 학생: ★★★★★\n2번 학생: ★★★\n3번 학생: ★"
# - stdin: "2\n80\n60"
#   expected_stdout: "1번 학생: ★★★★\n2번 학생: ★★"

# for + if/elif를 사용하세요.
n = int(input())
# TODO
