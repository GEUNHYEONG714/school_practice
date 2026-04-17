"""
TITLE: 자기 기술 수열 (Look-and-Say)
DIFFICULTY: hard
TAGS: algorithm, string, while, for, if
EVAL: stdio

DESCRIPTION:
양의 정수 N을 입력받아, Look-and-Say 수열의 N번째 항을 출력하시오.

Look-and-Say 수열은 이전 항을 "읽어서" 다음 항을 만든다:
- 1번째 항: 1
- 2번째 항: 11 (1이 1개)
- 3번째 항: 21 (1이 2개)
- 4번째 항: 1211 (2가 1개, 1이 1개)
- 5번째 항: 111221 (1이 1개, 2가 1개, 2가 2개, 1이 1개)

1번째부터 N번째까지 각 항을 한 줄에 하나씩 출력한다.

예시:
- 입력: `5` → 수열의 1~5번째 항 출력
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "1\n11\n21\n1211\n111221"
# - stdin: "1"
#   expected_stdout: "1"
# - stdin: "7"
#   expected_stdout: "1\n11\n21\n1211\n111221\n312211\n13112221"

# 문자열을 순회하며 연속 같은 문자의 개수를 세어 다음 항 구성
n = int(input())
# TODO
