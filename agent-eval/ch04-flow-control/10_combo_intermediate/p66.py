"""
TITLE: 동전 거스름돈 (최소 개수)
DIFFICULTY: hard
TAGS: algorithm, greedy, for, if, coin
EVAL: stdio

DESCRIPTION:
거스름돈 금액(10의 배수)을 입력받아
500원, 100원, 50원, 10원 동전을 사용하여
최소 동전 개수로 거슬러 주는 결과를 출력하세요.
(리스트/딕셔너리/함수 사용 금지)

출력 형식 (각 줄):
```
500원: X개
100원: X개
50원: X개
10원: X개
총 동전 수: Y개
```

예시:
- 입력: `1260` → 500원: 2개 / 100원: 2개 / 50원: 1개 / 10원: 1개 / 총 동전 수: 6개
"""
# META_TESTS:
# - stdin: "1260"
#   expected_stdout: "500원: 2개\n100원: 2개\n50원: 1개\n10원: 1개\n총 동전 수: 6개"
# - stdin: "500"
#   expected_stdout: "500원: 1개\n100원: 0개\n50원: 0개\n10원: 0개\n총 동전 수: 1개"
# - stdin: "30"
#   expected_stdout: "500원: 0개\n100원: 0개\n50원: 0개\n10원: 3개\n총 동전 수: 3개"

# 금액을 입력받아 최소 동전 수로 거슬러 주세요.
money = int(input())
# TODO
