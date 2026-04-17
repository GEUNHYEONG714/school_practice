"""
TITLE: 이메일 유효성 검사
DIFFICULTY: easy
TAGS: for, if, string, flag
EVAL: stdio

DESCRIPTION:
문자열을 입력받아 이메일 유효성을 간단히 검사합니다.

"@"와 "."이 모두 포함되어 있으면 "유효", 하나라도 없으면 "무효"를 출력하시오.

for문으로 문자열을 순회하며 "@"와 "."의 존재 여부를 확인하세요.

예시:
- 입력: `user@example.com` → 출력: `유효`
- 입력: `user.example` → "@"가 없으므로 출력: `무효`
"""
# META_TESTS:
# - stdin: "user@example.com"
#   expected_stdout: "유효"
# - stdin: "user.example"
#   expected_stdout: "무효"
# - stdin: "user@domain"
#   expected_stdout: "무효"

# for문으로 문자열을 순회하며 플래그를 사용하세요.
s = input()
# TODO
