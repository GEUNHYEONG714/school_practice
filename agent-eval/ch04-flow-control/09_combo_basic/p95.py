"""
TITLE: 달력 출력
DIFFICULTY: hard
TAGS: for, if, while, combo
EVAL: stdio

DESCRIPTION:
시작 요일과 마지막 날짜를 입력받아 달력 형태로 출력하시오.

첫째 줄: 시작 요일 (1=월, 2=화, ..., 7=일)
둘째 줄: 마지막 날짜 (28, 30, 31 등)

출력 형식:
- 첫 줄에 `월  화  수  목  금  토  일` 헤더를 출력합니다.
- 각 날짜는 2자리 오른쪽 정렬, 구분자는 공백 2칸입니다.
- 시작 요일 전까지는 빈 칸(`    `)으로 채웁니다.
- 일요일(7번째 칸) 뒤에서 줄바꿈합니다.

예시:
- 입력: `3`, `31` (수요일 시작, 31일까지)
"""
# META_TESTS:
# - stdin: "1\n7"
#   expected_stdout: "월  화  수  목  금  토  일\n 1   2   3   4   5   6   7"
# - stdin: "6\n10"
#   expected_stdout: "월  화  수  목  금  토  일\n                     1   2\n 3   4   5   6   7   8   9\n10"
# - stdin: "3\n14"
#   expected_stdout: "월  화  수  목  금  토  일\n             1   2   3   4   5\n 6   7   8   9  10  11  12\n13  14"

# 헤더 출력 후, 시작 요일에 맞춰 날짜를 배치하세요.
start_day = int(input())
last_date = int(input())
# TODO
