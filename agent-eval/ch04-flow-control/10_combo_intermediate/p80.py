"""
TITLE: 별 원형
DIFFICULTY: hard
TAGS: pattern, nested-loop, circle, math, star
EVAL: stdio

DESCRIPTION:
정수 N(홀수)을 입력받아 N*N 격자에서 원에 가까운 별 패턴을 출력하세요.
- 반지름 R = N // 2, 중심 좌표는 (R, R)입니다.
- 각 위치 (r, c)에서 중심까지의 거리의 제곱을 구합니다:
  dist_sq = (r - R) * (r - R) + (c - R) * (c - R)
- 거리의 제곱이 (R-0.5)*(R-0.5) 이상이고 (R+0.5)*(R+0.5) 이하이면 `*`를 출력합니다.
- 그렇지 않으면 공백(` `)을 출력합니다.
- 각 행에서 마지막 `*` 이후의 공백은 출력하지 않습니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시 (N=5, R=2):
```
 ***
*   *
*   *
*   *
 ***
```

예시 (N=7, R=3):
```
  ***
 *   *
*     *
*     *
*     *
 *   *
  ***
```
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: " ***\n*   *\n*   *\n*   *\n ***"
# - stdin: "7"
#   expected_stdout: "  ***\n *   *\n*     *\n*     *\n*     *\n *   *\n  ***"
# - stdin: "3"
#   expected_stdout: "***\n* *\n***"

# N*N 격자에서 원형 별 패턴을 출력하세요.
n = int(input())
# TODO
