"""
TITLE: 빈 사각형 (대각선 포함)
DIFFICULTY: hard
TAGS: pattern, nested-loop, border, diagonal
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 N*N 크기의 사각형을 출력하세요.
- 테두리(첫 행, 마지막 행, 첫 열, 마지막 열)는 `*`로 출력합니다.
- 두 대각선(왼위→오아래, 오위→왼아래)도 `*`로 출력합니다.
- 나머지 위치는 공백(` `)으로 출력합니다.
- 각 행에서 마지막 `*` 이후의 공백은 출력하지 않습니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시 (N=5):
```
*****
** **
* * *
** **
*****
```

예시 (N=7):
```
*******
**   **
* * * *
*  *  *
* * * *
**   **
*******
```
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "*****\n** **\n* * *\n** **\n*****"
# - stdin: "7"
#   expected_stdout: "*******\n**   **\n* * * *\n*  *  *\n* * * *\n**   **\n*******"
# - stdin: "3"
#   expected_stdout: "***\n***\n***"

# N*N 사각형에서 테두리와 대각선만 별로 출력하세요.
n = int(input())
# TODO
