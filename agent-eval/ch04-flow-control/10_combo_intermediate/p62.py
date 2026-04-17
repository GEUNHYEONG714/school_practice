"""
TITLE: 두 수의 곱 최대
DIFFICULTY: hard
TAGS: algorithm, search, nested_for, max
EVAL: stdio

DESCRIPTION:
첫 줄에 정수 N(2 이상), 이후 N줄에 걸쳐 정수를 하나씩 입력받아
서로 다른 두 수의 곱이 최대인 값을 출력하세요.
(리스트/딕셔너리/함수 사용 금지)

힌트: 이중 for문으로 모든 쌍을 비교합니다.
두 번째 입력 시 매 반복마다 다시 입력을 받을 수 없으므로,
N개의 수를 공백 구분 한 줄로 입력받고 split 후 이중 for를 사용합니다.

예시:
- 입력: `4` / `3 -5 2 7` → 출력: `21`
- 입력: `3` / `-4 -3 1` → 출력: `12`
"""
# META_TESTS:
# - stdin: "4\n3 -5 2 7"
#   expected_stdout: "21"
# - stdin: "3\n-4 -3 1"
#   expected_stdout: "12"
# - stdin: "5\n1 2 3 4 5"
#   expected_stdout: "20"

# N개 정수 중 서로 다른 위치의 두 수 곱이 최대인 값을 구하세요.
n = int(input())
# TODO
