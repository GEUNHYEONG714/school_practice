"""
TITLE: 미니 체스 (나이트 이동)
DIFFICULTY: hard
TAGS: game, chess, knight, nested-loop, if, boundary
EVAL: stdio

DESCRIPTION:
8x8 체스판에서 나이트의 현재 위치(행, 열)를 공백으로 구분하여 입력받습니다 (0~7).
나이트가 이동할 수 있는 모든 위치를 출력합니다.
나이트는 L자 형태로 이동: (±1,±2) 또는 (±2,±1)
체스판 범위(0~7)를 벗어나는 위치는 제외합니다.
출력 순서: 행이 작은 것부터, 행이 같으면 열이 작은 것부터.
각 위치는 한 줄에 하나씩 "행 열" 형태로 출력합니다.
(리스트/딕셔너리/함수 사용 금지, 변수만 사용)

예시:
- 입력: `0 0` → 출력:
  1 2
  2 1
- 입력: `4 4` → 8개 위치 출력
"""
# META_TESTS:
# - stdin: "0 0"
#   expected_stdout: "1 2\n2 1"
# - stdin: "4 4"
#   expected_stdout: "2 3\n2 5\n3 2\n3 6\n5 2\n5 6\n6 3\n6 5"
# - stdin: "7 7"
#   expected_stdout: "5 6\n6 5"

# 나이트 이동: 현재 위치에서 갈 수 있는 모든 위치를 출력하세요.
line = input().split()
r, c = int(line[0]), int(line[1])
# TODO
