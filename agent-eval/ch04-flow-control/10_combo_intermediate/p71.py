"""
TITLE: 숫자 나선 (반시계)
DIFFICULTY: hard
TAGS: pattern, nested-loop, spiral, math
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 N*N 크기의 반시계 방향 나선형 숫자 패턴을 출력하세요.
- 1부터 N*N까지의 숫자를 반시계 방향(아래→오른쪽→위→왼쪽)으로 채웁니다.
- 시작 위치는 왼쪽 위(0,0)이며, 처음에 아래 방향으로 진행합니다.
- 각 숫자는 공백 한 칸으로 구분합니다.
- 숫자 출력 시 가장 큰 수의 자릿수에 맞춰 오른쪽 정렬합니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시 (N=3):
```
1 8 7
2 9 6
3 4 5
```

예시 (N=4):
```
 1 12 11 10
 2 13 16  9
 3 14 15  8
 4  5  6  7
```
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "1 8 7\n2 9 6\n3 4 5"
# - stdin: "4"
#   expected_stdout: " 1 12 11 10\n 2 13 16  9\n 3 14 15  8\n 4  5  6  7"
# - stdin: "2"
#   expected_stdout: "1 4\n2 3"

# N*N 반시계 방향 나선형 숫자를 출력하세요.
n = int(input())
# TODO
