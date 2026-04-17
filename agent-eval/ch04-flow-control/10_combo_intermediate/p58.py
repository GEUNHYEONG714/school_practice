"""
TITLE: 디지털 근
DIFFICULTY: hard
TAGS: algorithm, math, while, for
EVAL: stdio

DESCRIPTION:
양의 정수를 입력받아, 디지털 근(Digital Root)을 구하시오.

디지털 근이란 각 자릿수의 합을 구하는 과정을 한 자리 수가 될 때까지
반복한 최종 결과이다.

매 단계의 과정을 출력한다.
`단계 K: 자릿수 합 계산 A → B`
(A는 현재 수를 각 자릿수로 분해한 덧셈식, B는 합)
마지막에 `디지털 근: X` 을 출력한다.

이미 한 자리 수인 경우 과정 없이 `디지털 근: X` 만 출력한다.

예시:
- 입력: `9875` → 9+8+7+5=29 → 2+9=11 → 1+1=2
"""
# META_TESTS:
# - stdin: "9875"
#   expected_stdout: "단계 1: 자릿수 합 계산 9+8+7+5 → 29\n단계 2: 자릿수 합 계산 2+9 → 11\n단계 3: 자릿수 합 계산 1+1 → 2\n디지털 근: 2"
# - stdin: "493"
#   expected_stdout: "단계 1: 자릿수 합 계산 4+9+3 → 16\n단계 2: 자릿수 합 계산 1+6 → 7\n디지털 근: 7"
# - stdin: "5"
#   expected_stdout: "디지털 근: 5"

# while로 자릿수 합을 반복하되, 덧셈식 문자열도 함께 구성
num = int(input())
# TODO
