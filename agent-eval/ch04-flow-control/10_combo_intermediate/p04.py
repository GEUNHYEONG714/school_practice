"""
TITLE: 피보나치 수열
DIFFICULTY: hard
TAGS: algorithm, math, fibonacci, loop
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 피보나치 수열의 0번째부터 N번째 항까지 출력합니다.
첫 줄: `피보나치 수열 (0~N번째):` (N은 입력값)
둘째 줄: 항들을 공백으로 구분하여 출력 (끝에 공백 포함)

예시:
- 입력: `10` → 출력:
```
피보나치 수열 (0~10번째):
0 1 1 2 3 5 8 13 21 34 55
```
"""
# META_TESTS:
# - stdin: "10"
#   expected_stdout: "피보나치 수열 (0~10번째):\n0 1 1 2 3 5 8 13 21 34 55 "
# - stdin: "5"
#   expected_stdout: "피보나치 수열 (0~5번째):\n0 1 1 2 3 5 "
# - stdin: "0"
#   expected_stdout: "피보나치 수열 (0~0번째):\n0 "

# 0번째부터 N번째 피보나치 수를 출력하세요.
n = int(input())
# TODO
