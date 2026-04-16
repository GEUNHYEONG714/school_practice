"""
TITLE: 빈 다이아몬드
DIFFICULTY: hard
TAGS: pattern, nested_loop
EVAL: stdio

DESCRIPTION:
홀수 n을 입력받아 테두리만 별(*)이고 안쪽은 공백인 다이아몬드를 출력합니다.
꼭짓점(별이 1개인 줄)은 별을 하나만 출력합니다.

예시 (n=7):
```
   *
  * *
 *   *
*     *
 *   *
  * *
   *
```
"""
# META_TESTS:
# - stdin: "7"
#   expected_stdout: "   *\n  * *\n *   *\n*     *\n *   *\n  * *\n   *"
# - stdin: "5"
#   expected_stdout: "  *\n * *\n*   *\n * *\n  *"
# - stdin: "3"
#   expected_stdout: " *\n* *\n *"

# 빈 다이아몬드를 출력하세요.
n = int(input())
# TODO
