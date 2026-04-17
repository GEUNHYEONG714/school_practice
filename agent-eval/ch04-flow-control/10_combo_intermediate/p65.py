"""
TITLE: 물통 채우기
DIFFICULTY: hard
TAGS: simulation, for, if, overflow
EVAL: stdio

DESCRIPTION:
첫 줄에 물통 용량 C와 물 개수 N(공백 구분),
이후 N줄에 물의 양을 하나씩 입력받습니다.
물을 순서대로 부어서 넘치는 시점(1-based)과 넘친 양을 출력하세요.
끝까지 넘치지 않으면 `안 넘침`을 출력합니다.
(리스트/딕셔너리/함수 사용 금지)

출력 형식: `X번째에서 넘침! 넘친 양: Y`

예시:
- 입력: `10 3` / `4` / `5` / `3` → 출력: `3번째에서 넘침! 넘친 양: 2`
- 입력: `20 2` / `5` / `10` → 출력: `안 넘침`
"""
# META_TESTS:
# - stdin: "10 3\n4\n5\n3"
#   expected_stdout: "3번째에서 넘침! 넘친 양: 2"
# - stdin: "20 2\n5\n10"
#   expected_stdout: "안 넘침"
# - stdin: "5 4\n1\n2\n3\n4"
#   expected_stdout: "3번째에서 넘침! 넘친 양: 1"

# 물통에 물을 순서대로 부어 넘치는 시점을 찾으세요.
c, n = map(int, input().split())
# TODO
