"""
TITLE: 1~N 소수 출력
DIFFICULTY: hard
TAGS: algorithm, math, prime, loop
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 2부터 N 사이의 모든 소수를 공백으로 구분하여 한 줄에 출력하고(끝에 공백 포함),
다음 줄에 `소수 개수: K` 형식으로 소수 개수를 출력합니다.

예시:
- 입력: `30` → 출력:
```
2 3 5 7 11 13 17 19 23 29
소수 개수: 10
```
"""
# META_TESTS:
# - stdin: "30"
#   expected_stdout: "2 3 5 7 11 13 17 19 23 29 \n소수 개수: 10"
# - stdin: "10"
#   expected_stdout: "2 3 5 7 \n소수 개수: 4"
# - stdin: "2"
#   expected_stdout: "2 \n소수 개수: 1"

# 2부터 N까지 각 수가 소수인지 판별하여 출력하세요.
n = int(input())
# TODO
