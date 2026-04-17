"""
TITLE: 진수 덧셈기
DIFFICULTY: hard
TAGS: binary, string, loop, if, carry, math
EVAL: stdio

DESCRIPTION:
2진수 문자열 두 개를 각 줄에 하나씩 입력받아 덧셈 결과를 2진수 문자열로 출력합니다.
int() 변환 없이 문자열 상태에서 직접 자릿수별 덧셈과 올림(carry)을 처리하세요.
결과의 앞에 불필요한 0이 없어야 합니다 (단, 결과가 0이면 "0" 출력).
(리스트/딕셔너리/함수 사용 금지, 변수만 사용)

예시:
- 입력: `1010` / `1011` → 출력: `10101`
- 입력: `111` / `1` → 출력: `1000`
"""
# META_TESTS:
# - stdin: "1010\n1011"
#   expected_stdout: "10101"
# - stdin: "111\n1"
#   expected_stdout: "1000"
# - stdin: "0\n0"
#   expected_stdout: "0"

# 2진수 덧셈: int 변환 없이 문자열로 직접 계산하세요.
bin1 = input()
bin2 = input()
# TODO
