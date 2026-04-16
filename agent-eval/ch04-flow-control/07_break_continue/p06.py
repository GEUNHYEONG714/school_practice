"""
TITLE: 짝수만 누적
DIFFICULTY: medium
TAGS: for, continue, accumulator

EVAL: stdio

DESCRIPTION:
5개의 정수를 한 줄씩 입력받아 홀수는 건너뛰고 짝수만 합계에 누적합니다.
- 홀수일 때는 `홀수는 건너뜁니다`를 출력한 뒤 `continue`로 건너뜁니다.
- 마지막에 `짝수 합계: 값` 형식으로 합계를 출력합니다.
(출력은 `print("짝수 합계:", total)` — 콤마로 공백 하나 포함)

예시:
- 입력: `3\n4\n7\n10\n2` → 출력:
  ```
  홀수는 건너뜁니다
  홀수는 건너뜁니다
  짝수 합계: 16
  ```
"""
# META_TESTS:
# - stdin: "3\n4\n7\n10\n2"
#   expected_stdout: "홀수는 건너뜁니다\n홀수는 건너뜁니다\n짝수 합계: 16"
# - stdin: "1\n3\n5\n7\n9"
#   expected_stdout: "홀수는 건너뜁니다\n홀수는 건너뜁니다\n홀수는 건너뜁니다\n홀수는 건너뜁니다\n홀수는 건너뜁니다\n짝수 합계: 0"
# - stdin: "2\n4\n6\n8\n10"
#   expected_stdout: "짝수 합계: 30"

# for i in range(5): num = int(input()); if num % 2 != 0: print("홀수는 건너뜁니다"); continue; total += num
total = 0
# TODO
