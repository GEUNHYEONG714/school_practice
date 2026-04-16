"""
TITLE: 숫자 맞추기 게임
DIFFICULTY: medium
TAGS: while, break, if-elif-else

EVAL: stdio

DESCRIPTION:
정답은 `42`입니다. 숫자를 반복해서 입력받아 정답과 비교합니다.
- 입력한 수가 정답보다 작으면 `더 큰 수를 입력하세요`
- 입력한 수가 정답보다 크면 `더 작은 수를 입력하세요`
- 정답이면 `정답입니다!`를 출력하고 종료합니다.

예시:
- 입력: `30\n50\n42` → 출력:
  ```
  더 큰 수를 입력하세요
  더 작은 수를 입력하세요
  정답입니다!
  ```
"""
# META_TESTS:
# - stdin: "30\n50\n42"
#   expected_stdout: "더 큰 수를 입력하세요\n더 작은 수를 입력하세요\n정답입니다!"
# - stdin: "42"
#   expected_stdout: "정답입니다!"
# - stdin: "100\n10\n40\n42"
#   expected_stdout: "더 작은 수를 입력하세요\n더 큰 수를 입력하세요\n더 큰 수를 입력하세요\n정답입니다!"

# while True 안에서 정답일 때 break 하세요.
answer = 42
# TODO
