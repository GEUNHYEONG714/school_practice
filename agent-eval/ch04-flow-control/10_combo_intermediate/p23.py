"""
TITLE: 지그재그 패턴
DIFFICULTY: hard
TAGS: pattern, nested_loop
EVAL: stdio

DESCRIPTION:
줄 수 n과 한 줄 숫자 개수 m을 각 줄에 입력받아, 1부터 연속된 숫자를 한 줄에 m개씩 출력합니다.
홀수 줄은 왼쪽 정렬, 짝수 줄은 오른쪽 정렬(전체 너비 m*2)합니다.
숫자는 공백으로 구분합니다.

예시 (n=4, m=3):
```
1 2 3
      4 5 6
7 8 9
      10 11 12
```
"""
# META_TESTS:
# - stdin: "4\n3"
#   expected_stdout: "1 2 3\n      4 5 6\n7 8 9\n      10 11 12"
# - stdin: "2\n2"
#   expected_stdout: "1 2\n   3 4"
# - stdin: "3\n2"
#   expected_stdout: "1 2\n   3 4\n5 6"

# 지그재그 패턴을 출력하세요.
n = int(input())
m = int(input())
# TODO
