"""
TITLE: 별 마름모
DIFFICULTY: medium
TAGS: for, if, range, print, string-repetition
EVAL: stdio

DESCRIPTION:
홀수 N을 입력받아 N줄짜리 마름모를 출력하시오.

출력 규칙:
- 각 줄은 공백과 별(*)로 구성
- 가운데 줄이 가장 넓고 (N개의 별), 위아래로 대칭
- 별 사이에 공백 없이 붙여서 출력

예시 (N=5):
```
  *
 ***
*****
 ***
  *
```
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "  *\n ***\n*****\n ***\n  *"
# - stdin: "3"
#   expected_stdout: " *\n***\n *"
# - stdin: "7"
#   expected_stdout: "   *\n  ***\n *****\n*******\n *****\n  ***\n   *"

# 홀수 N을 입력받아 마름모를 출력하세요.
n = int(input())
# TODO
