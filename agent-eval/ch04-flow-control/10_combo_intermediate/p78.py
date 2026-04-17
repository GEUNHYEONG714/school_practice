"""
TITLE: 테두리 삼각형
DIFFICULTY: hard
TAGS: pattern, nested-loop, triangle, border, star
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 테두리만 있는 삼각형 패턴을 출력하세요.
- 총 N행을 출력합니다.
- 첫 행(꼭대기)은 별 1개를 가운데 정렬합니다.
- 중간 행들은 양쪽 끝에만 별을 출력하고, 안쪽은 공백입니다.
- 마지막 행(밑변)은 별 (2*N-1)개를 연속 출력합니다.
- 줄 끝에 불필요한 공백이 없어야 합니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시 (N=3):
```
  *
 * *
*****
```

예시 (N=5):
```
    *
   * *
  *   *
 *     *
*********
```
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "  *\n * *\n*****"
# - stdin: "5"
#   expected_stdout: "    *\n   * *\n  *   *\n *     *\n*********"
# - stdin: "4"
#   expected_stdout: "   *\n  * *\n *   *\n*******"

# 테두리만 있는 삼각형 패턴을 출력하세요.
n = int(input())
# TODO
