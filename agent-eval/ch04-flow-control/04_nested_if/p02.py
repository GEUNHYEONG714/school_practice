"""
TITLE: 로그인 시스템
DIFFICULTY: easy
TAGS: nested, if, else, string

EVAL: stdio

DESCRIPTION:
아이디와 비밀번호를 순서대로 입력받아 결과를 출력하시오.
정답 아이디는 `admin`, 정답 비밀번호는 `1234`입니다.

- 아이디 맞음:
  - 비밀번호 맞음: `로그인 성공!`
  - 비밀번호 틀림: `비밀번호가 틀렸습니다.`
- 아이디 틀림: `ID가 존재하지 않습니다.`

예시:
- 입력: `admin\n1234` → 출력: `로그인 성공!`
- 입력: `admin\n5678` → 출력: `비밀번호가 틀렸습니다.`
- 입력: `guest\n1234` → 출력: `ID가 존재하지 않습니다.`
"""
# META_TESTS:
# - stdin: "admin\n1234"
#   expected_stdout: "로그인 성공!"
# - stdin: "admin\n5678"
#   expected_stdout: "비밀번호가 틀렸습니다."
# - stdin: "guest\n1234"
#   expected_stdout: "ID가 존재하지 않습니다."

# 중첩 if문으로 아이디를 먼저, 그 안에서 비밀번호를 확인하세요.
user_id = input()
password = input()
# TODO
