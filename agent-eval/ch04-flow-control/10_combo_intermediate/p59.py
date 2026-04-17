"""
TITLE: 소수 간격 찾기
DIFFICULTY: hard
TAGS: algorithm, math, prime, for, while, if
EVAL: stdio

DESCRIPTION:
양의 정수 N(N >= 6)을 입력받아, 2 이상 N 이하의 소수들 사이에서
가장 큰 간격(차이)을 가진 연속한 소수 쌍을 출력하시오.

출력 형식:
```
소수 목록: 2 3 5 7 ...
최대 간격: A와 B 사이 (간격: C)
```

간격이 같은 쌍이 여러 개이면 첫 번째(가장 작은) 쌍을 출력한다.

예시:
- 입력: `30` → 23과 29 사이 간격 6이 최대
"""
# META_TESTS:
# - stdin: "30"
#   expected_stdout: "소수 목록: 2 3 5 7 11 13 17 19 23 29\n최대 간격: 23과 29 사이 (간격: 6)"
# - stdin: "10"
#   expected_stdout: "소수 목록: 2 3 5 7\n최대 간격: 3과 5 사이 (간격: 2)"
# - stdin: "50"
#   expected_stdout: "소수 목록: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47\n최대 간격: 23과 29 사이 (간격: 6)"

# 소수 판별 후 연속 소수 간 차이를 비교하여 최대 간격 추적
n = int(input())
# TODO
