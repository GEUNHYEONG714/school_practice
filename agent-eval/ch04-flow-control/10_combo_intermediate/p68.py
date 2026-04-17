"""
TITLE: 점프 게임
DIFFICULTY: hard
TAGS: algorithm, greedy, for, if, jump
EVAL: stdio

DESCRIPTION:
첫 줄에 정수 N, 둘째 줄에 N개의 점프력(공백 구분, 0 이상 정수)을 입력받아
첫 번째 칸에서 출발하여 마지막 칸에 도달 가능한지 판별하세요.
(리스트/딕셔너리/함수 사용 금지)

- 각 칸의 값은 해당 칸에서 최대로 점프할 수 있는 거리
- 도달 가능하면 `YES`, 불가능하면 `NO` 출력
- 힌트: max_reach 변수로 도달 가능한 최대 인덱스를 관리

예시:
- 입력: `5` / `2 3 1 1 4` → 출력: `YES`
- 입력: `5` / `3 2 1 0 4` → 출력: `NO`
"""
# META_TESTS:
# - stdin: "5\n2 3 1 1 4"
#   expected_stdout: "YES"
# - stdin: "5\n3 2 1 0 4"
#   expected_stdout: "NO"
# - stdin: "1\n0"
#   expected_stdout: "YES"

# 첫 칸에서 마지막 칸까지 도달 가능 여부를 판별하세요.
n = int(input())
# TODO
