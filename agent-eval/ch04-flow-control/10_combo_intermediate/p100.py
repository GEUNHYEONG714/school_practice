"""
TITLE: 미니 인터프리터
DIFFICULTY: hard
TAGS: interpreter, string, loop, if, parsing
EVAL: stdio

DESCRIPTION:
첫 줄에 명령어 개수 N을 입력받고, 이후 N개의 명령어를 한 줄씩 입력받습니다.
지원하는 명령어:
- SET x 값: 변수 x에 정수 값을 저장
- ADD x 값: 변수 x에 정수 값을 더함
- PRINT x: 변수 x의 값을 출력
변수는 x, y 두 개만 사용합니다 (초기값 0).
(리스트/딕셔너리/함수 사용 금지, 변수만 사용)

예시:
- 입력:
  4
  SET x 5
  ADD x 3
  SET y 10
  PRINT x
- 출력: 8

- 입력:
  5
  SET x 10
  SET y 20
  ADD x 5
  PRINT x
  PRINT y
- 출력:
  15
  20
"""
# META_TESTS:
# - stdin: "4\nSET x 5\nADD x 3\nSET y 10\nPRINT x"
#   expected_stdout: "8"
# - stdin: "5\nSET x 10\nSET y 20\nADD x 5\nPRINT x\nPRINT y"
#   expected_stdout: "15\n20"
# - stdin: "6\nSET x 1\nSET y 2\nADD x 10\nADD y 20\nPRINT x\nPRINT y"
#   expected_stdout: "11\n22"

# 미니 인터프리터: SET, ADD, PRINT 명령어를 처리하세요.
n = int(input())
# TODO
