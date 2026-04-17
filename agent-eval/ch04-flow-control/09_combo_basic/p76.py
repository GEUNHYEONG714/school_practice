"""
TITLE: 문자열 압축 (Run-Length Encoding)
DIFFICULTY: medium
TAGS: for, if, string, counter
EVAL: stdio

DESCRIPTION:
문자열을 입력받아 연속으로 같은 문자가 반복되는 부분을 "문자개수" 형태로 압축하여 출력하시오.

예시:
- 입력: `aabbbcc` → 출력: `a2b3c2`
- 입력: `abc` → 각 문자 1개씩 → 출력: `a1b1c1`

for문으로 문자열을 순회하며 이전 문자와 비교하세요.
"""
# META_TESTS:
# - stdin: "aabbbcc"
#   expected_stdout: "a2b3c2"
# - stdin: "abc"
#   expected_stdout: "a1b1c1"
# - stdin: "aaaa"
#   expected_stdout: "a4"

# for문으로 순회하며 이전 문자와 현재 문자를 비교하세요.
s = input()
result = ""
# TODO
