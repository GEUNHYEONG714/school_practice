"""
TITLE: 골드바흐의 추측
DIFFICULTY: hard
TAGS: algorithm, math, prime, loop
EVAL: stdio

DESCRIPTION:
4 이상의 짝수 N을 입력받아, 두 소수의 합으로 표현하는 모든 경우를 `N = i + j` 형식으로 출력합니다.
(i <= j, i는 2부터 N//2까지)

예시:
- 입력: `20` → 출력:
```
20 = 3 + 17
20 = 7 + 13
```
"""
# META_TESTS:
# - stdin: "20"
#   expected_stdout: "20 = 3 + 17\n20 = 7 + 13"
# - stdin: "10"
#   expected_stdout: "10 = 3 + 7\n10 = 5 + 5"
# - stdin: "4"
#   expected_stdout: "4 = 2 + 2"

# N을 두 소수의 합으로 표현하는 모든 경우를 출력하세요.
N = int(input())
# TODO
