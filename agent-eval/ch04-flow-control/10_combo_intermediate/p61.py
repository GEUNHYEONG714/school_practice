"""
TITLE: 최대 연속 합
DIFFICULTY: hard
TAGS: algorithm, kadane, for, if, max
EVAL: stdio

DESCRIPTION:
첫 줄에 정수 N, 둘째 줄에 N개의 정수(공백 구분)를 입력받아
연속 부분합 중 최대값을 출력하세요.
(리스트/딕셔너리/함수 사용 금지, 변수만 사용)

카데인 알고리즘 변형:
- current_sum에 현재 값을 더하되, 현재 값이 더 크면 현재 값부터 다시 시작
- max_sum은 항상 최대값을 유지

예시:
- 입력: `5` / `2 -3 4 -1 2` → 출력: `5`
- 입력: `4` / `-1 -2 -3 -4` → 출력: `-1`
"""
# META_TESTS:
# - stdin: "5\n2 -3 4 -1 2"
#   expected_stdout: "5"
# - stdin: "4\n-1 -2 -3 -4"
#   expected_stdout: "-1"
# - stdin: "6\n1 2 3 -10 5 6"
#   expected_stdout: "11"

# 첫 줄에 N, 둘째 줄에 N개 정수를 입력받아 최대 연속 부분합을 구하세요.
n = int(input())
# TODO
