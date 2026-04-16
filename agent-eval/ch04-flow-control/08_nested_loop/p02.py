"""
TITLE: 숫자 피라미드
DIFFICULTY: medium
TAGS: nested-loop, for, pattern, numbers

DESCRIPTION:
줄 수 N을 입력받아, i번째 줄에 1부터 i까지의 숫자를 이어붙여 출력하는
숫자 피라미드를 출력하시오.

예시:
- 입력: `3` → 출력: `1\n12\n123`
- 입력: `5` → 출력: `1\n12\n123\n1234\n12345`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "1\n12\n123"
# - stdin: "5"
#   expected_stdout: "1\n12\n123\n1234\n12345"
# - stdin: "1"
#   expected_stdout: "1"

# print(j, end="")을 사용해 줄바꿈 없이 이어서 출력하세요.
n = int(input())
# TODO
