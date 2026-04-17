"""
TITLE: ROT13 암호화
DIFFICULTY: medium
TAGS: for, if, elif, string, ord, chr
EVAL: stdio

DESCRIPTION:
문자열을 입력받아 ROT13 암호화를 적용하여 출력하시오.

ROT13 규칙:
- 알파벳을 13칸 뒤로 밀어 변환 (a→n, b→o, ..., n→a, z→m)
- 대문자와 소문자 모두 각각 변환하되 대소문자를 유지
- 알파벳이 아닌 문자는 그대로 유지

ord()와 chr()을 사용하여 문자 코드를 계산하세요.

예시:
- 입력: `Hello` → 출력: `Uryyb`
- 입력: `abc` → 출력: `nop`
"""
# META_TESTS:
# - stdin: "Hello"
#   expected_stdout: "Uryyb"
# - stdin: "abc"
#   expected_stdout: "nop"
# - stdin: "Hello, World!"
#   expected_stdout: "Uryyb, Jbeyq!"

# for문으로 순회하며 ord(), chr()을 사용해 13칸 밀기를 구현하세요.
s = input()
result = ""
# TODO
