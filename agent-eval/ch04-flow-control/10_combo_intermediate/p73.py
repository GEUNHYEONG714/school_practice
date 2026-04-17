"""
TITLE: 숫자 모래시계
DIFFICULTY: hard
TAGS: pattern, nested-loop, hourglass, number
EVAL: stdio

DESCRIPTION:
정수 N을 입력받아 숫자로 채운 모래시계 패턴을 출력하세요.
- 총 행 수는 N입니다 (N >= 3).
- 첫 행은 1부터 N까지, 중간으로 갈수록 양쪽에서 숫자가 줄어듭니다.
- 가운데를 지나면 다시 양쪽으로 숫자가 늘어납니다.
- 각 행에서 줄어든 만큼 앞에 공백(2칸씩)을 넣어 가운데 정렬합니다.
- 숫자는 공백 한 칸으로 구분합니다.
- 줄 끝에 불필요한 공백이 없어야 합니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시 (N=5):
```
1 2 3 4 5
  2 3 4
    3
  2 3 4
1 2 3 4 5
```

예시 (N=3):
```
1 2 3
  2
1 2 3
```
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "1 2 3 4 5\n  2 3 4\n    3\n  2 3 4\n1 2 3 4 5"
# - stdin: "3"
#   expected_stdout: "1 2 3\n  2\n1 2 3"
# - stdin: "4"
#   expected_stdout: "1 2 3 4\n  2 3\n  2 3\n1 2 3 4"

# 숫자로 채운 모래시계 패턴을 출력하세요.
n = int(input())
# TODO
