"""
TITLE: 미니 스프레드시트
DIFFICULTY: hard
TAGS: simulation, spreadsheet, nested-loop, for, if
EVAL: stdio

DESCRIPTION:
N행 M열의 격자 숫자를 입력받아 각 행의 합과 각 열의 합을 출력하세요.
- 첫 줄에 N과 M을 공백으로 구분하여 입력받습니다 (N, M은 2 또는 3).
- 이후 N줄에 M개의 정수를 공백으로 구분하여 입력받습니다.
- 먼저 격자를 그대로 출력합니다.
- 빈 줄 후 각 행의 합을 출력합니다: `행1 합: X`
- 빈 줄 후 각 열의 합을 출력합니다: `열1 합: X`
- N과 M이 최대 3이므로 변수 v11~v33으로 저장할 수 있습니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시:
- 입력: `2 3`, `1 2 3`, `4 5 6` → 출력:
```
1 2 3
4 5 6

행1 합: 6
행2 합: 15

열1 합: 5
열2 합: 7
열3 합: 9
```
"""
# META_TESTS:
# - stdin: "2 3\n1 2 3\n4 5 6"
#   expected_stdout: "1 2 3\n4 5 6\n\n행1 합: 6\n행2 합: 15\n\n열1 합: 5\n열2 합: 7\n열3 합: 9"
# - stdin: "2 2\n10 20\n30 40"
#   expected_stdout: "10 20\n30 40\n\n행1 합: 30\n행2 합: 70\n\n열1 합: 40\n열2 합: 60"
# - stdin: "3 2\n1 1\n2 2\n3 3"
#   expected_stdout: "1 1\n2 2\n3 3\n\n행1 합: 2\n행2 합: 4\n행3 합: 6\n\n열1 합: 6\n열2 합: 6"

# N*M 격자 숫자를 입력받아 행 합과 열 합을 출력하세요.
n, m = input().split()
n = int(n)
m = int(m)
# TODO
