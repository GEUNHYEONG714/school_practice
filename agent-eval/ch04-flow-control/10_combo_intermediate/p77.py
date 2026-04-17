"""
TITLE: 별 계단
DIFFICULTY: hard
TAGS: pattern, nested-loop, staircase, star
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 계단 모양의 별 패턴을 출력하세요.
- 총 N행을 출력합니다.
- i번째 행(1부터 시작)은 (i-1)개의 공백 후 i개의 별(`*`)을 출력합니다.
- 각 행이 오른쪽으로 한 칸씩 밀려난 직각삼각형 모양입니다.
- 줄 끝에 불필요한 공백이 없어야 합니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시 (N=3):
```
*
 **
  ***
```

예시 (N=5):
```
*
 **
  ***
   ****
    *****
```
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "*\n **\n  ***"
# - stdin: "5"
#   expected_stdout: "*\n **\n  ***\n   ****\n    *****"
# - stdin: "4"
#   expected_stdout: "*\n **\n  ***\n   ****"

# 계단 모양의 별 패턴을 출력하세요.
n = int(input())
# TODO
