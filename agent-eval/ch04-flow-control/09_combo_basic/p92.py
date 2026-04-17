"""
TITLE: 숫자 빙고
DIFFICULTY: hard
TAGS: for, if, nested-loop, range, input, comparison
EVAL: stdio

DESCRIPTION:
1~25 중 5개의 숫자를 입력받고,
5x5 빙고판(1~25)에서 해당 숫자를 X로 표시하여 출력하시오.

출력 규칙:
- 5x5 격자를 한 줄에 5개씩 출력
- 같은 줄의 값은 탭(\\t)으로 구분
- 입력된 숫자 위치는 `X`로 표시, 나머지는 숫자 그대로 출력

예시 (입력: 1 7 13 19 25):
```
X\t2\t3\t4\t5
6\tX\t8\t9\t10
11\t12\tX\t14\t15
16\t17\t18\tX\t20
21\t22\t23\t24\tX
```
"""
# META_TESTS:
# - stdin: "1\n7\n13\n19\n25"
#   expected_stdout: "X\t2\t3\t4\t5\n6\tX\t8\t9\t10\n11\t12\tX\t14\t15\n16\t17\t18\tX\t20\n21\t22\t23\t24\tX"
# - stdin: "1\n2\n3\n4\n5"
#   expected_stdout: "X\tX\tX\tX\tX\n6\t7\t8\t9\t10\n11\t12\t13\t14\t15\n16\t17\t18\t19\t20\n21\t22\t23\t24\t25"
# - stdin: "5\n10\n15\n20\n25"
#   expected_stdout: "1\t2\t3\t4\tX\n6\t7\t8\t9\tX\n11\t12\t13\t14\tX\n16\t17\t18\t19\tX\n21\t22\t23\t24\tX"

# 5개 숫자를 입력받아 5x5 빙고판에서 해당 숫자를 X로 표시하세요.
# TODO
