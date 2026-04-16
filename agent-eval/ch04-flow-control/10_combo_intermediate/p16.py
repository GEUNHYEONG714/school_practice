"""
TITLE: 자릿수가 같은 수 (Repdigit)
DIFFICULTY: hard
TAGS: algorithm, math, digit, loop
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 1부터 N 사이에서 모든 자릿수가 동일한 수를 한 줄에 하나씩 출력합니다.
(한 자리 수 1~9도 포함)

예시:
- 입력: `50` → 출력:
```
1
2
3
4
5
6
7
8
9
11
22
33
44
```
"""
# META_TESTS:
# - stdin: "50"
#   expected_stdout: "1\n2\n3\n4\n5\n6\n7\n8\n9\n11\n22\n33\n44"
# - stdin: "15"
#   expected_stdout: "1\n2\n3\n4\n5\n6\n7\n8\n9\n11"
# - stdin: "120"
#   expected_stdout: "1\n2\n3\n4\n5\n6\n7\n8\n9\n11\n22\n33\n44\n55\n66\n77\n88\n99\n111"

# 1부터 N 사이에서 모든 자릿수가 동일한 수를 출력하세요.
N = int(input())
# TODO
