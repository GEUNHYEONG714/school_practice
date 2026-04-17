"""
TITLE: 배열 출력
DIFFICULTY: easy
TAGS: for, nested-loop, range, print, tab
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 1부터 N*N까지의 숫자를 N열씩 줄바꿈하며 출력하시오.

출력 규칙:
- 같은 줄의 숫자는 탭(\\t)으로 구분
- N개씩 출력 후 줄바꿈

예시 (N=3):
```
1\t2\t3
4\t5\t6
7\t8\t9
```
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "1\t2\t3\n4\t5\t6\n7\t8\t9"
# - stdin: "2"
#   expected_stdout: "1\t2\n3\t4"
# - stdin: "4"
#   expected_stdout: "1\t2\t3\t4\n5\t6\t7\t8\n9\t10\t11\t12\n13\t14\t15\t16"

# N을 입력받아 1~N*N 숫자를 N열씩 탭 구분으로 출력하세요.
n = int(input())
# TODO
