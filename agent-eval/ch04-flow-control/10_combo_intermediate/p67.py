"""
TITLE: 최대 직사각형
DIFFICULTY: hard
TAGS: algorithm, search, nested_for, max, rectangle
EVAL: stdio

DESCRIPTION:
첫 줄에 정수 N, 둘째 줄에 N개의 높이(공백 구분, 양의 정수)를 입력받아
연속된 막대로 만들 수 있는 최대 직사각형 넓이를 출력하세요.
(리스트/딕셔너리/함수 사용 금지)

- 이중 for문을 사용: 시작 위치 i, 끝 위치 j를 정하고
  구간 내 최소 높이 × 구간 너비(j-i+1)로 넓이를 계산
- 힌트: 입력을 공백으로 split하여 이중 for에서 인덱스 접근 대신
  매번 다시 순회하며 최소 높이를 갱신합니다.

예시:
- 입력: `6` / `2 1 5 6 2 3` → 출력: `10`
- 입력: `4` / `3 3 3 3` → 출력: `12`
"""
# META_TESTS:
# - stdin: "6\n2 1 5 6 2 3"
#   expected_stdout: "10"
# - stdin: "4\n3 3 3 3"
#   expected_stdout: "12"
# - stdin: "3\n1 1 1"
#   expected_stdout: "3"

# 연속 막대로 만들 수 있는 최대 직사각형 넓이를 구하세요.
n = int(input())
# TODO
