"""
TITLE: 별 화살표
DIFFICULTY: hard
TAGS: pattern, nested-loop, arrow, star
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 오른쪽을 가리키는 화살표 모양의 별 패턴을 출력하세요.
- 총 행 수는 2*N-1 입니다.
- 위쪽 절반은 1개부터 N개까지 별이 증가합니다.
- 아래쪽 절반은 N-1개부터 1개까지 별이 감소합니다.
- 별은 공백 한 칸으로 구분합니다.
- 줄 끝에 불필요한 공백이 없어야 합니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시 (N=3):
```
*
* *
* * *
* *
*
```

예시 (N=4):
```
*
* *
* * *
* * * *
* * *
* *
*
```
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "*\n* *\n* * *\n* *\n*"
# - stdin: "4"
#   expected_stdout: "*\n* *\n* * *\n* * * *\n* * *\n* *\n*"
# - stdin: "2"
#   expected_stdout: "*\n* *\n*"

# 오른쪽을 가리키는 화살표 모양의 별 패턴을 출력하세요.
n = int(input())
# TODO
