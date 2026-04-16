"""
TITLE: 비밀번호 확인
DIFFICULTY: medium
TAGS: while, break, counter

EVAL: stdio

DESCRIPTION:
비밀번호는 `python`입니다. 최대 3번까지 입력받습니다.
- 맞으면 `로그인 성공!`을 출력하고 종료합니다.
- 틀리면 `틀렸습니다. 남은 기회: N번` 을 출력합니다(N은 남은 기회).
- 3번 모두 틀리면 마지막에 `계정이 잠겼습니다` 를 출력합니다.
(출력 형식: `print("틀렸습니다. 남은 기회:", str(chance) + "번")` — 콤마 뒤 공백 포함)

예시:
- 입력: `abc\n123\nhello` → 출력:
  ```
  틀렸습니다. 남은 기회: 2번
  틀렸습니다. 남은 기회: 1번
  계정이 잠겼습니다
  ```
- 입력: `abc\npython` → 출력:
  ```
  틀렸습니다. 남은 기회: 2번
  로그인 성공!
  ```
"""
# META_TESTS:
# - stdin: "abc\n123\nhello"
#   expected_stdout: "틀렸습니다. 남은 기회: 2번\n틀렸습니다. 남은 기회: 1번\n계정이 잠겼습니다"
# - stdin: "abc\npython"
#   expected_stdout: "틀렸습니다. 남은 기회: 2번\n로그인 성공!"
# - stdin: "python"
#   expected_stdout: "로그인 성공!"

# chance = 3 로 시작, while chance > 0: 입력 → 비교 → 맞으면 break, 틀리면 chance -= 1
password = "python"
# TODO
