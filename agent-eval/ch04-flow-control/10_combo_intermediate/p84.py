"""
TITLE: 신호등 시뮬레이션
DIFFICULTY: hard
TAGS: simulation, traffic-light, for, if, modular
EVAL: stdio

DESCRIPTION:
총 시간과 신호 주기를 입력받아 각 초의 신호등 상태를 출력하세요.
- 첫 줄에 총 시간 T(초)를 입력받습니다.
- 둘째 줄에 초록/노랑/빨강 신호 지속 시간을 공백으로 구분하여 입력받습니다.
- 신호 순서: 초록 → 노랑 → 빨강을 반복합니다.
- 0초부터 T-1초까지 각 초의 신호를 출력합니다.
- 출력 형식: `X초: 신호`  (신호는 초록/노랑/빨강)
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시:
- 입력: `7`, `2 1 3` → 출력:
```
0초: 초록
1초: 초록
2초: 노랑
3초: 빨강
4초: 빨강
5초: 빨강
6초: 초록
```
"""
# META_TESTS:
# - stdin: "7\n2 1 3"
#   expected_stdout: "0초: 초록\n1초: 초록\n2초: 노랑\n3초: 빨강\n4초: 빨강\n5초: 빨강\n6초: 초록"
# - stdin: "4\n1 1 1"
#   expected_stdout: "0초: 초록\n1초: 노랑\n2초: 빨강\n3초: 초록"
# - stdin: "3\n3 2 1"
#   expected_stdout: "0초: 초록\n1초: 초록\n2초: 초록"

# 총 시간과 신호 주기를 입력받아 각 초의 신호를 출력하세요.
t = int(input())
g, y, r = input().split()
g = int(g)
y = int(y)
r = int(r)
# TODO
