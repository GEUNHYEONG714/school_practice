"""
TITLE: 패턴 반복 출력
DIFFICULTY: medium
TAGS: nested-for, string

DESCRIPTION:
첫 줄에 문자열, 둘째 줄에 반복 횟수 n을 입력받아
각 글자를 n번씩 반복하여 한 줄에 이어서 출력하시오. 마지막에 줄바꿈이 있어야 합니다.

예시:
- 입력: `abc`, `3` → 출력: `aaabbbccc`
"""
# META_TESTS:
# - stdin: "abc\n3"
#   expected_stdout: "aaabbbccc"
# - stdin: "xy\n2"
#   expected_stdout: "xxyy"
# - stdin: "a\n5"
#   expected_stdout: "aaaaa"

# 바깥 for는 각 글자, 안쪽 for는 n번 출력
text = input()
n = int(input())
# TODO
print()
