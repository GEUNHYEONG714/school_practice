"""
TITLE: 디지털 시계
DIFFICULTY: easy
TAGS: if, arithmetic, format, print
EVAL: stdio

DESCRIPTION:
총 초(seconds)를 입력받아 HH:MM:SS 형식으로 변환하여 출력하시오.
각 자리는 2자리로 0을 채워 출력합니다. (예: 02:03:05)

예시:
- 입력: `7385` → `02:03:05`
- 입력: `60` → `00:01:00`
"""
# META_TESTS:
# - stdin: "7385"
#   expected_stdout: "02:03:05"
# - stdin: "60"
#   expected_stdout: "00:01:00"
# - stdin: "86399"
#   expected_stdout: "23:59:59"

# 총 초를 입력받아 HH:MM:SS 형식으로 출력하세요.
total_seconds = int(input())
# TODO
