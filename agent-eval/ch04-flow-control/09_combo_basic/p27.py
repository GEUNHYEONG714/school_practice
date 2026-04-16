"""
TITLE: 약수의 개수
DIFFICULTY: medium
TAGS: for, if, range, modulo

DESCRIPTION:
숫자를 입력받아 그 숫자의 약수를 한 줄에 하나씩 오름차순으로 출력하고,
마지막에 `약수의 개수: N` 형태로 약수의 개수를 출력하시오.

예시:
- 입력: `12` → 출력: `1`, `2`, `3`, `4`, `6`, `12`, `약수의 개수: 6`
"""
# META_TESTS:
# - stdin: "12"
#   expected_stdout: "1\n2\n3\n4\n6\n12\n약수의 개수: 6"
# - stdin: "7"
#   expected_stdout: "1\n7\n약수의 개수: 2"
# - stdin: "1"
#   expected_stdout: "1\n약수의 개수: 1"

# 1부터 num까지 반복하며 나머지가 0이면 약수
num = int(input())
count = 0
# TODO
print("약수의 개수:", count)
