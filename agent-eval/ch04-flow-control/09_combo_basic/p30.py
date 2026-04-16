"""
TITLE: 수 분류기
DIFFICULTY: medium
TAGS: for, if, elif, else

DESCRIPTION:
10개의 숫자를 한 줄에 하나씩 입력받아 양수의 합, 음수의 합, 0의 개수를 구하시오.
출력 형식:
`양수의 합: P`
`음수의 합: N`
`0의 개수: Z`

예시:
- 입력: 5, -3, 0, 7, -1, 0, 10, -8, 3, 0 → 양수 합 25, 음수 합 -12, 0 개수 3
"""
# META_TESTS:
# - stdin: "5\n-3\n0\n7\n-1\n0\n10\n-8\n3\n0"
#   expected_stdout: "양수의 합: 25\n음수의 합: -12\n0의 개수: 3"
# - stdin: "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
#   expected_stdout: "양수의 합: 55\n음수의 합: 0\n0의 개수: 0"

# 10번 반복하며 양수/음수/0 분류
pos_sum = 0
neg_sum = 0
zero_count = 0
# TODO
print("양수의 합:", pos_sum)
print("음수의 합:", neg_sum)
print("0의 개수:", zero_count)
