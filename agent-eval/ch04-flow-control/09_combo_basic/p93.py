"""
TITLE: 비밀번호 생성기
DIFFICULTY: easy
TAGS: for, string, combo
EVAL: stdio

DESCRIPTION:
비밀번호 길이 N을 입력받아, 알파벳 소문자와 숫자를 교대로 배치한 비밀번호를 생성하시오.

알파벳은 a부터 순서대로, 숫자는 1부터 순서대로 사용합니다.
알파벳이 z를 넘으면 다시 a부터, 숫자가 9를 넘으면 다시 0부터 반복합니다.

홀수 번째 자리(1,3,5,...)에는 알파벳, 짝수 번째 자리(2,4,6,...)에는 숫자를 배치합니다.

예시:
- 입력: `6` → 출력: `a1b2c3`
- 입력: `5` → 출력: `a1b2c`
- 입력: `10` → 출력: `a1b2c3d4e5`
"""
# META_TESTS:
# - stdin: "6"
#   expected_stdout: "a1b2c3"
# - stdin: "5"
#   expected_stdout: "a1b2c"
# - stdin: "10"
#   expected_stdout: "a1b2c3d4e5"

# for문으로 한 글자씩 생성하세요.
n = int(input())
# TODO
