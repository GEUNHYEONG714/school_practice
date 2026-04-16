"""
TITLE: 모래시계 패턴
DIFFICULTY: hard
TAGS: pattern, nested_loop
EVAL: stdio

DESCRIPTION:
홀수 n을 입력받아 모래시계 모양을 별(*)로 출력합니다.
위쪽 역삼각형(가운데 포함)과 아래쪽 삼각형(가운데 제외)을 조합합니다.

예시 (n=7):
```
*******
 *****
  ***
   *
  ***
 *****
*******
```
"""
# META_TESTS:
# - stdin: "7"
#   expected_stdout: "*******\n *****\n  ***\n   *\n  ***\n *****\n*******"
# - stdin: "5"
#   expected_stdout: "*****\n ***\n  *\n ***\n*****"
# - stdin: "3"
#   expected_stdout: "***\n *\n***"

# 모래시계 패턴을 출력하세요.
n = int(input())
# TODO
