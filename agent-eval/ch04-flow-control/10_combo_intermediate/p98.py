"""
TITLE: 타일 채우기
DIFFICULTY: hard
TAGS: fibonacci, dp, loop, math, tile
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아, 가로 N칸을 1칸짜리 타일과 2칸짜리 타일로 채우는 경우의 수를 출력합니다.
이는 피보나치 수열의 변형입니다:
- N=1: 1가지 (1)
- N=2: 2가지 (1+1, 2)
- N=3: 3가지 (1+1+1, 1+2, 2+1)
- N=k: f(k-1) + f(k-2)
(리스트/딕셔너리/함수 사용 금지, 변수만 사용)

예시:
- 입력: `5` → 출력: `8`
- 입력: `10` → 출력: `89`
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "8"
# - stdin: "10"
#   expected_stdout: "89"
# - stdin: "1"
#   expected_stdout: "1"

# 타일 채우기: 가로 N칸을 1칸/2칸 타일로 채우는 경우의 수를 구하세요.
n = int(input())
# TODO
