"""
TITLE: 해밍수
DIFFICULTY: hard
TAGS: algorithm, math, loop
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 1부터 N 사이의 해밍수를 한 줄에 하나씩 출력합니다.
해밍수: 2, 3, 5 이외의 소인수를 갖지 않는 양의 정수

예시:
- 입력: `30` → 출력:
```
1
2
3
4
5
6
8
9
10
12
15
16
18
20
24
25
27
30
```
"""
# META_TESTS:
# - stdin: "10"
#   expected_stdout: "1\n2\n3\n4\n5\n6\n8\n9\n10"
# - stdin: "15"
#   expected_stdout: "1\n2\n3\n4\n5\n6\n8\n9\n10\n12\n15"
# - stdin: "6"
#   expected_stdout: "1\n2\n3\n4\n5\n6"

# 1부터 N 사이의 해밍수를 출력하세요.
N = int(input())
# TODO
