"""
TITLE: 균형점 찾기
DIFFICULTY: hard
TAGS: algorithm, search, for, if, balance
EVAL: stdio

DESCRIPTION:
첫 줄에 정수 N, 둘째 줄에 N개의 정수(공백 구분)를 입력받아
왼쪽 합과 오른쪽 합이 같아지는 위치(0-based 인덱스)를 출력하세요.
균형점이 여러 개면 가장 작은 인덱스를, 없으면 `-1`을 출력합니다.
(리스트/딕셔너리/함수 사용 금지)

- 균형점 위치의 값은 왼쪽/오른쪽 합에 포함하지 않음
- 힌트: 전체 합을 먼저 구한 뒤, 왼쪽 합을 누적하며 오른쪽 합과 비교

예시:
- 입력: `5` / `1 2 3 2 1` → 출력: `2`
- 입력: `3` / `1 2 3` → 출력: `-1`
"""
# META_TESTS:
# - stdin: "5\n1 2 3 2 1"
#   expected_stdout: "2"
# - stdin: "3\n1 2 3"
#   expected_stdout: "-1"
# - stdin: "1\n10"
#   expected_stdout: "0"

# 왼쪽 합 == 오른쪽 합인 균형점 위치를 찾으세요.
n = int(input())
# TODO
