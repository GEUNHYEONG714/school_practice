"""
TITLE: 암호 만들기
DIFFICULTY: medium
TAGS: for, if, ord, chr

DESCRIPTION:
문자열을 입력받아 각 알파벳 글자를 다음 글자로 변환한 암호를 출력하시오.
- 소문자: a→b, ..., z→a (순환)
- 대문자: A→B, ..., Z→A (순환)
- 알파벳이 아닌 글자는 그대로 둔다.
출력 형식: `암호: ...`

예시:
- 입력: `hello` → 출력: `암호: ifmmp`
- 입력: `xyz` → 출력: `암호: yza`
"""
# META_TESTS:
# - stdin: "hello"
#   expected_stdout: "암호: ifmmp"
# - stdin: "xyz"
#   expected_stdout: "암호: yza"
# - stdin: "Hi Z!"
#   expected_stdout: "암호: Ij A!"

# ord/chr와 z/Z 순환 처리
text = input()
result = ""
# TODO
print("암호:", result)
