"""
TITLE: 기온별 외출 안내
DIFFICULTY: easy
TAGS: if, else, comparison, print

EVAL: stdio

DESCRIPTION:
기온(정수)을 입력받아 아래 규칙에 따라 출력하시오.

- 기온이 0 미만이면 두 줄 출력: `영하입니다`, `빙판길을 조심하세요`
- 기온이 0 이상이면 한 줄 출력: `영상입니다`
- 어떤 경우든 마지막에는 `외출 준비 완료!`를 출력

예시:
- 입력: `-5` → 출력: `영하입니다\n빙판길을 조심하세요\n외출 준비 완료!`
- 입력: `12` → 출력: `영상입니다\n외출 준비 완료!`
- 입력: `0` → 출력: `영상입니다\n외출 준비 완료!`
"""
# META_TESTS:
# - stdin: "-5"
#   expected_stdout: "영하입니다\n빙판길을 조심하세요\n외출 준비 완료!"
# - stdin: "12"
#   expected_stdout: "영상입니다\n외출 준비 완료!"
# - stdin: "0"
#   expected_stdout: "영상입니다\n외출 준비 완료!"

# < 연산자 사용. 블록 안/밖 구분에 주의하세요.
temp = int(input())
# TODO
