"""
TITLE: 나르시시스트 수
DIFFICULTY: hard
TAGS: algorithm, math, while, for, if
EVAL: stdio

DESCRIPTION:
양의 정수 N(자릿수)을 입력받아, N자리 나르시시스트 수를 모두 출력하시오.

나르시시스트 수란 각 자릿수를 자릿수 개수(N)만큼 거듭제곱하여 더한 값이
자기 자신과 같은 수이다.
예: 153은 3자리이며, 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153이므로 나르시시스트 수이다.

각 나르시시스트 수를 한 줄에 하나씩 출력한다.
해당하는 수가 없으면 아무것도 출력하지 않는다.

예시:
- 입력: `3` → 3자리 나르시시스트 수 출력
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "153\n370\n371\n407"
# - stdin: "1"
#   expected_stdout: "1\n2\n3\n4\n5\n6\n7\n8\n9"
# - stdin: "4"
#   expected_stdout: "1634\n8208\n9474"

# N자리 범위(10^(N-1) ~ 10^N - 1)를 순회하며 각 자릿수의 N제곱 합 비교
n = int(input())
# TODO
