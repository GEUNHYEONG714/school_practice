"""
TITLE: 다이아몬드
DIFFICULTY: medium
TAGS: nested-loop, for, pattern, stars

DESCRIPTION:
크기 N을 입력받아 다이아몬드를 출력하시오.
위쪽 삼각형은 1줄부터 N줄까지, 아래쪽 역삼각형은 N-1줄부터 1줄까지 이어 붙입니다.
i번째 줄(1부터 시작)에는 공백 (N-i)개 + 별 (2*i-1)개를 출력합니다.

예시:
- 입력: `2` → 출력: ` *\n***\n *`
- 입력: `3` → 출력: `  *\n ***\n*****\n ***\n  *`
- 입력: `4` → 출력: `   *\n  ***\n *****\n*******\n *****\n  ***\n   *`
"""
# META_TESTS:
# - stdin: "2"
#   expected_stdout: " *\n***\n *"
# - stdin: "3"
#   expected_stdout: "  *\n ***\n*****\n ***\n  *"
# - stdin: "1"
#   expected_stdout: "*"

# 위쪽 삼각형과 아래쪽 역삼각형을 각각 for문으로 출력하세요.
n = int(input())
# TODO
