"""
TITLE: 나비 모양 패턴
DIFFICULTY: hard
TAGS: pattern, nested_loop
EVAL: stdio

DESCRIPTION:
홀수 n을 입력받아 나비 모양을 별(*)로 출력합니다.
왼쪽 삼각형과 오른쪽 삼각형이 좌우 대칭으로 결합된 형태이며, 가운데 줄은 별이 연속됩니다.

예시 (n=5):
```
*       *
**     **
*********
**     **
*       *
```
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "*       *\n**     **\n*********\n**     **\n*       *"
# - stdin: "3"
#   expected_stdout: "*   *\n***\n*   *"
# - stdin: "7"
#   expected_stdout: "*           *\n**         **\n***       ***\n*************\n***       ***\n**         **\n*           *"

# 나비 모양 패턴을 출력하세요.
n = int(input())
# TODO
