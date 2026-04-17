"""
TITLE: 숫자 합 게임
DIFFICULTY: easy
TAGS: for, if, accumulator, comparison
EVAL: stdio

DESCRIPTION:
첫 줄에 숫자 개수 N을 입력받고, 이어서 N개의 정수를 한 줄씩 입력받습니다.
양수의 합, 음수의 합, 전체 합을 각각 출력하시오. (0은 양수/음수 어디에도 포함하지 않음)

출력 형식:
`양수 합: X`
`음수 합: X`
`전체 합: X`

예시:
- 입력: `4\n3\n-2\n5\n-1` → 양수 합 8, 음수 합 -3, 전체 합 5
"""
# META_TESTS:
# - stdin: "4\n3\n-2\n5\n-1"
#   expected_stdout: "양수 합: 8\n음수 합: -3\n전체 합: 5"
# - stdin: "3\n10\n20\n30"
#   expected_stdout: "양수 합: 60\n음수 합: 0\n전체 합: 60"
# - stdin: "5\n-1\n0\n-3\n2\n4"
#   expected_stdout: "양수 합: 6\n음수 합: -4\n전체 합: 2"

# N개의 숫자를 입력받아 양수 합, 음수 합, 전체 합을 출력하세요.
n = int(input())
# TODO
