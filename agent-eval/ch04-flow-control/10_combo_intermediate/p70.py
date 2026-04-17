"""
TITLE: 구간 최대값
DIFFICULTY: hard
TAGS: algorithm, sliding_window, for, if, max
EVAL: stdio

DESCRIPTION:
첫 줄에 정수 N과 구간 크기 K(공백 구분),
둘째 줄에 N개의 정수(공백 구분)를 입력받아
크기 K인 각 연속 구간의 최대값을 공백으로 구분하여 출력하세요.
(리스트/딕셔너리/함수 사용 금지)

- 구간 수: N - K + 1개
- 이중 for문으로 각 시작 위치마다 K개를 순회하며 최대값을 구합니다.
- 힌트: 입력 문자열을 split하여 인덱스로 접근

예시:
- 입력: `6 3` / `1 3 2 5 4 6` → 출력: `3 5 5 6`
- 입력: `5 2` / `4 2 7 1 3` → 출력: `4 7 7 3`
"""
# META_TESTS:
# - stdin: "6 3\n1 3 2 5 4 6"
#   expected_stdout: "3 5 5 6"
# - stdin: "5 2\n4 2 7 1 3"
#   expected_stdout: "4 7 7 3"
# - stdin: "4 1\n5 3 8 2"
#   expected_stdout: "5 3 8 2"

# 크기 K인 각 연속 구간의 최대값을 구하세요.
n, k = map(int, input().split())
# TODO
