"""
TITLE: 하샤드 수
DIFFICULTY: hard
TAGS: algorithm, math, while, for, if
EVAL: stdio

DESCRIPTION:
양의 정수 N을 입력받아, 1 이상 N 이하의 하샤드 수를 모두 출력하시오.

하샤드 수란 자기 자신이 각 자릿수의 합으로 나누어 떨어지는 수이다.
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 하샤드 수이다.

각 하샤드 수를 한 줄에 하나씩 출력한다.

예시:
- 입력: `12` → 1부터 12까지의 하샤드 수 출력
"""
# META_TESTS:
# - stdin: "12"
#   expected_stdout: "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n12"
# - stdin: "21"
#   expected_stdout: "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n12\n18\n20\n21"
# - stdin: "1"
#   expected_stdout: "1"

# 각 수에 대해 자릿수 합을 구한 뒤 나누어 떨어지는지 확인
n = int(input())
# TODO
