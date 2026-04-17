"""
TITLE: 지뢰 찾기 (간단)
DIFFICULTY: hard
TAGS: game, grid, nested-loop, if, mine
EVAL: stdio

DESCRIPTION:
3x3 격자의 지뢰 정보를 3줄에 걸쳐 입력받습니다.
각 줄에는 3개의 값이 공백으로 구분되어 있으며, 0은 빈 칸, 1은 지뢰입니다.
각 칸에 대해 주변 8방향의 지뢰 수를 계산하여 출력하되, 지뢰인 칸은 *로 표시합니다.
각 줄의 값은 공백으로 구분합니다.
(리스트/딕셔너리/함수 사용 금지, 변수만 사용)

예시:
- 입력:
  0 1 0
  0 0 0
  1 0 0
- 출력:
  1 * 1
  2 2 1
  * 1 0
"""
# META_TESTS:
# - stdin: "0 1 0\n0 0 0\n1 0 0"
#   expected_stdout: "1 * 1\n2 2 1\n* 1 0"
# - stdin: "1 1 1\n1 1 1\n1 1 1"
#   expected_stdout: "* * *\n* * *\n* * *"
# - stdin: "0 0 0\n0 1 0\n0 0 0"
#   expected_stdout: "1 1 1\n1 * 1\n1 1 1"

# 3x3 지뢰찾기: 각 칸의 주변 지뢰 수를 출력하세요 (지뢰는 *)
# 3줄에 걸쳐 각 줄에 3개의 값(0 또는 1)을 입력받으세요.
r0c0, r0c1, r0c2 = input().split()
r1c0, r1c1, r1c2 = input().split()
r2c0, r2c1, r2c2 = input().split()
# TODO
