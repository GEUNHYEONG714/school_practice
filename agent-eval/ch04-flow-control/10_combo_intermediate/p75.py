"""
TITLE: 별 피라미드 (가운데 정렬)
DIFFICULTY: hard
TAGS: pattern, nested-loop, pyramid, star
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 가운데 정렬된 별 피라미드를 출력하세요.
- 총 N행을 출력합니다.
- i번째 행(1부터 시작)은 (N-i)개의 공백 후 (2*i-1)개의 별(`*`)을 출력합니다.
- 줄 끝에 불필요한 공백이 없어야 합니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시 (N=3):
```
  *
 ***
*****
```

예시 (N=5):
```
    *
   ***
  *****
 *******
*********
```
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "  *\n ***\n*****"
# - stdin: "5"
#   expected_stdout: "    *\n   ***\n  *****\n *******\n*********"
# - stdin: "4"
#   expected_stdout: "   *\n  ***\n *****\n*******"

# 가운데 정렬된 별 피라미드를 출력하세요.
n = int(input())
# TODO
