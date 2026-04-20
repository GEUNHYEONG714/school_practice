"""
TITLE: 최대값 찾기 (-1 종료)
DIFFICULTY: easy
TAGS: while, sentinel, max

EVAL: stdio

DESCRIPTION:
숫자를 반복해서 입력받고, `-1`이 입력되면 종료합니다.
입력한 숫자 중 가장 큰 값을 `최대값: 값` 형식(f-string)으로 출력하시오.
만약 `-1`만 입력된 경우 `입력한 숫자가 없습니다.`를 출력하시오.

예시:
- 입력: `5\n23\n17\n8\n-1` → 출력: `최대값: 23`
- 입력: `-1` → 출력: `입력한 숫자가 없습니다.`
"""
# META_TESTS:
# - stdin: "5\n23\n17\n8\n-1"
#   expected_stdout: "최대값: 23"
# - stdin: "-1"
#   expected_stdout: "입력한 숫자가 없습니다."
# - stdin: "10\n-1"
#   expected_stdout: "최대값: 10"

# 힌트: max_val = None으로 초기화한 뒤 첫 입력에서 값을 채우거나,
# 첫 입력값으로 max_val을 초기화한 뒤 이후 입력과 비교해 더 크면 갱신하세요.
# (max_val = -1 같은 상수 초기화는 음수만 입력되는 경우 오답이 될 수 있습니다.)
# TODO
