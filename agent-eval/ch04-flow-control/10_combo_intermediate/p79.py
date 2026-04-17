"""
TITLE: 숫자 회전 사각형
DIFFICULTY: hard
TAGS: pattern, nested-loop, concentric, number
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 N*N 크기의 동심 사각형 숫자 패턴을 출력하세요.
- 가장 바깥쪽 테두리는 가장 큰 수(층 수)로 채웁니다.
- 안쪽으로 들어갈수록 1씩 감소합니다.
- 가장 안쪽은 1입니다.
- 층 수는 (N+1)//2 입니다.
- 숫자는 공백 한 칸으로 구분합니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시 (N=5):
```
3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
```

예시 (N=4):
```
2 2 2 2
2 1 1 2
2 1 1 2
2 2 2 2
```
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "3 3 3 3 3\n3 2 2 2 3\n3 2 1 2 3\n3 2 2 2 3\n3 3 3 3 3"
# - stdin: "4"
#   expected_stdout: "2 2 2 2\n2 1 1 2\n2 1 1 2\n2 2 2 2"
# - stdin: "3"
#   expected_stdout: "2 2 2\n2 1 2\n2 2 2"

# 동심 사각형 숫자 패턴을 출력하세요.
n = int(input())
# TODO
