"""
TITLE: 미니 성적 관리
DIFFICULTY: medium
TAGS: for, if, accumulator
EVAL: stdio

DESCRIPTION:
5명의 점수를 차례로 입력받아 평균과 최고점을 출력하시오.

출력 형식:
`평균: 평균값`
`최고점: 최고점값`

평균은 합계 / 5 로 계산합니다 (실수 그대로 출력).

예시:
- 입력: `80\n95\n70\n88\n60` → 출력: `평균: 78.6\n최고점: 95`
"""
# META_TESTS:
# - stdin: "80\n95\n70\n88\n60"
#   expected_stdout: "평균: 78.6\n최고점: 95"
# - stdin: "100\n100\n100\n100\n100"
#   expected_stdout: "평균: 100.0\n최고점: 100"

# for + if + 누적 변수를 사용하세요.
total = 0
best = 0
# TODO
