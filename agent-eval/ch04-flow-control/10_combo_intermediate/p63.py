"""
TITLE: 가장 긴 증가 구간
DIFFICULTY: hard
TAGS: algorithm, search, for, if, max
EVAL: stdio

DESCRIPTION:
첫 줄에 정수 N, 둘째 줄에 N개의 정수(공백 구분)를 입력받아
연속으로 증가하는 가장 긴 구간의 길이를 출력하세요.
(리스트/딕셔너리/함수 사용 금지)

- 증가 구간: 이전 값보다 현재 값이 더 큰 연속 구간
- 구간 길이는 해당 구간에 포함된 원소의 수

예시:
- 입력: `7` / `1 3 5 2 4 6 8` → 출력: `4` (2→4→6→8)
- 입력: `5` / `5 4 3 2 1` → 출력: `1`
"""
# META_TESTS:
# - stdin: "7\n1 3 5 2 4 6 8"
#   expected_stdout: "4"
# - stdin: "5\n5 4 3 2 1"
#   expected_stdout: "1"
# - stdin: "6\n1 2 3 3 4 5"
#   expected_stdout: "3"

# N개 정수에서 연속으로 증가하는 가장 긴 구간의 길이를 구하세요.
n = int(input())
# TODO
