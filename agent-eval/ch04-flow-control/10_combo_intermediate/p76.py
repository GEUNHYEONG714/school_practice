"""
TITLE: 숫자 지그재그 삼각형
DIFFICULTY: hard
TAGS: pattern, nested-loop, zigzag, number
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 지그재그 숫자 삼각형을 출력하세요.
- 총 N행을 출력하며, i번째 행에는 i개의 숫자가 있습니다.
- 숫자는 1부터 연속으로 증가합니다.
- 홀수 행(1, 3, 5...)은 왼쪽에서 오른쪽으로 출력합니다.
- 짝수 행(2, 4, 6...)은 오른쪽에서 왼쪽(역순)으로 출력합니다.
- 숫자는 공백 한 칸으로 구분합니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시 (N=4):
```
1
3 2
4 5 6
10 9 8 7
```

예시 (N=5):
```
1
3 2
4 5 6
10 9 8 7
11 12 13 14 15
```
"""
# META_TESTS:
# - stdin: "4"
#   expected_stdout: "1\n3 2\n4 5 6\n10 9 8 7"
# - stdin: "3"
#   expected_stdout: "1\n3 2\n4 5 6"
# - stdin: "5"
#   expected_stdout: "1\n3 2\n4 5 6\n10 9 8 7\n11 12 13 14 15"

# 지그재그 숫자 삼각형을 출력하세요.
n = int(input())
# TODO
