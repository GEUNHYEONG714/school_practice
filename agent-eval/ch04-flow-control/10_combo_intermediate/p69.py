"""
TITLE: 봉우리 찾기
DIFFICULTY: hard
TAGS: algorithm, search, for, if, peak
EVAL: stdio

DESCRIPTION:
첫 줄에 정수 N, 둘째 줄에 N개의 정수(공백 구분)를 입력받아
봉우리(양옆보다 큰 값)의 개수를 출력하세요.
(리스트/딕셔너리/함수 사용 금지)

- 첫 번째 원소는 오른쪽만, 마지막 원소는 왼쪽만 비교
- 같은 값은 봉우리가 아님 (strictly greater)
- N이 1이면 그 자체가 봉우리 (개수 1)

예시:
- 입력: `7` / `1 3 2 5 4 6 1` → 출력: `3` (3, 5, 6이 봉우리)
- 입력: `5` / `1 2 3 4 5` → 출력: `1` (5만 봉우리)
"""
# META_TESTS:
# - stdin: "7\n1 3 2 5 4 6 1"
#   expected_stdout: "3"
# - stdin: "5\n1 2 3 4 5"
#   expected_stdout: "1"
# - stdin: "1\n10"
#   expected_stdout: "1"

# 봉우리(양옆보다 큰 값)의 개수를 구하세요.
n = int(input())
# TODO
