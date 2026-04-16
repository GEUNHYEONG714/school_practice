"""
TITLE: 파스칼 삼각형
DIFFICULTY: hard
TAGS: pattern, nested_loop, math
EVAL: stdio

DESCRIPTION:
줄 수 n을 입력받아 파스칼의 삼각형을 출력하시오.
각 줄의 숫자는 공백 하나로 구분하고, 가운데 정렬을 위해 앞쪽에 공백을 넣습니다.
이항계수는 누적 곱 방식으로 계산합니다: 다음 값 = 이전 값 * (줄번호 - k) // (k + 1)

출력 규칙:
- i번째 줄(0부터 시작) 앞에는 공백 `n - 1 - i`개를 출력
- 각 숫자 사이에는 공백 하나

예시:
- 입력: `3` → 출력: `  1\n 1 1\n1 2 1`
- 입력: `1` → 출력: `1`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "  1\n 1 1\n1 2 1"
# - stdin: "1"
#   expected_stdout: "1"
# - stdin: "5"
#   expected_stdout: "    1\n   1 1\n  1 2 1\n 1 3 3 1\n1 4 6 4 1"

# 각 줄에서 이항계수를 누적 곱으로 계산하세요.
n = int(input())
# TODO
