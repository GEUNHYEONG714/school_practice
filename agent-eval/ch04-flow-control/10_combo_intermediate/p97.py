"""
TITLE: 매직 스퀘어 검증
DIFFICULTY: hard
TAGS: game, magic-square, nested-loop, if, math
EVAL: stdio

DESCRIPTION:
3x3 격자의 숫자를 3줄에 걸쳐 입력받습니다.
각 줄에는 3개의 정수가 공백으로 구분되어 있습니다.
마방진인지 판별합니다: 모든 행의 합, 모든 열의 합, 두 대각선의 합이 모두 같으면 마방진입니다.
마방진이면 "YES"와 공통 합을, 아니면 "NO"를 출력합니다.
(리스트/딕셔너리/함수 사용 금지, 변수만 사용)

예시:
- 입력:
  2 7 6
  9 5 1
  4 3 8
- 출력:
  YES
  15
"""
# META_TESTS:
# - stdin: "2 7 6\n9 5 1\n4 3 8"
#   expected_stdout: "YES\n15"
# - stdin: "1 2 3\n4 5 6\n7 8 9"
#   expected_stdout: "NO"
# - stdin: "8 1 6\n3 5 7\n4 9 2"
#   expected_stdout: "YES\n15"

# 매직 스퀘어 검증: 3x3 격자가 마방진인지 판별하세요.
# 3줄에 걸쳐 각 줄에 3개의 정수를 입력받으세요.
r0c0, r0c1, r0c2 = input().split()
r1c0, r1c1, r1c2 = input().split()
r2c0, r2c1, r2c2 = input().split()
# TODO
