"""
TITLE: 타이머 (카운트다운)
DIFFICULTY: hard
TAGS: simulation, while, format
EVAL: stdio

DESCRIPTION:
분 단위 입력을 받아 `M분 SS초`부터 0초까지 카운트다운하여 한 줄씩 출력하시오.
- 초는 항상 두 자리(예: `05`)
- 초가 0이 되면 분을 1 감소시키고 초를 59로 설정
- 0분 0초 출력 후 `타이머 종료!` 출력

예시 (입력 0):
출력:
```
0분 00초
타이머 종료!
```
"""
# META_TESTS:
# - stdin: "0"
#   expected_stdout: "0분 00초\n타이머 종료!"

# 분과 초 변수로 관리하고 while True로 감소시키세요.
minutes = int(input())
seconds = 0
# TODO
