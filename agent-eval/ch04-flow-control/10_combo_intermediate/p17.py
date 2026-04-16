"""
TITLE: 증가수 찾기
DIFFICULTY: hard
TAGS: algorithm, math, digit, loop
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 10부터 N 사이에서 각 자릿수가 왼쪽에서 오른쪽으로 순증가하는 수를
한 줄에 하나씩 출력합니다. (두 자리 이상만)

예시:
- 입력: `30` → 출력:
```
12
13
14
15
16
17
18
19
23
24
25
26
27
28
29
```
"""
# META_TESTS:
# - stdin: "30"
#   expected_stdout: "12\n13\n14\n15\n16\n17\n18\n19\n23\n24\n25\n26\n27\n28\n29"
# - stdin: "20"
#   expected_stdout: "12\n13\n14\n15\n16\n17\n18\n19"
# - stdin: "15"
#   expected_stdout: "12\n13\n14\n15"

# 10부터 N 사이의 증가수를 출력하세요.
N = int(input())
# TODO
