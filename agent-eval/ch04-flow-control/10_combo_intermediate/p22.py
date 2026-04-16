"""
TITLE: 숫자 다이아몬드
DIFFICULTY: hard
TAGS: pattern, nested_loop
EVAL: stdio

DESCRIPTION:
홀수 n을 입력받아 다이아몬드 모양에 숫자를 채워 출력합니다.
각 줄에 1부터 시작하여 해당 줄의 숫자 개수만큼 증가했다가 감소합니다.

예시 (n=5):
```
  1
 121
12321
 121
  1
```
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "  1\n 121\n12321\n 121\n  1"
# - stdin: "3"
#   expected_stdout: " 1\n121\n 1"
# - stdin: "7"
#   expected_stdout: "   1\n  121\n 12321\n1234321\n 12321\n  121\n   1"

# 숫자 다이아몬드를 출력하세요.
n = int(input())
# TODO
