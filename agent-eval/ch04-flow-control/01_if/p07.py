"""
TITLE: 이름 확인
DIFFICULTY: easy
TAGS: if, string, print
EVAL: stdio

DESCRIPTION:
이름을 입력받아,
입력한 이름이 `홍길동`이면 `환영합니다, 홍길동님!`을 출력하시오.
다른 이름이면 아무것도 출력하지 마시오.

힌트: 문자열 비교에는 == 연산자를 사용합니다.

예시:
- 입력: `홍길동` → 출력: `환영합니다, 홍길동님!`
- 입력: `김철수` → 출력: (없음)
"""
# META_TESTS:
# - stdin: "홍길동"
#   expected_stdout: "환영합니다, 홍길동님!"
# - stdin: "김철수"
#   expected_stdout: ""

# 이름이 "홍길동"이면 환영 메시지를 출력하세요.
name = input()
# TODO
