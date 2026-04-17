"""
TITLE: 영화관 좌석
DIFFICULTY: medium
TAGS: if, arithmetic, string
EVAL: stdio

DESCRIPTION:
영화관 좌석번호(1~100)를 입력받아 열과 번호 형식으로 변환합니다.

좌석 배치:
- 한 열에 10석씩, 총 10열(A~J)
- 좌석 1~10: A열 1~10번
- 좌석 11~20: B열 1~10번
- ...
- 좌석 91~100: J열 1~10번

출력 형식: `좌석 N → X열 M번`

범위 밖(1 미만 또는 100 초과)이면: `잘못된 좌석번호입니다.`

예시:
- 입력: `25` → 출력: `좌석 25 → C열 5번`
- 입력: `100` → 출력: `좌석 100 → J열 10번`
"""
# META_TESTS:
# - stdin: "25"
#   expected_stdout: "좌석 25 → C열 5번"
# - stdin: "100"
#   expected_stdout: "좌석 100 → J열 10번"
# - stdin: "0"
#   expected_stdout: "잘못된 좌석번호입니다."

# 좌석번호를 열(A~J)과 번호(1~10)로 변환하세요
seat = int(input())
# TODO
