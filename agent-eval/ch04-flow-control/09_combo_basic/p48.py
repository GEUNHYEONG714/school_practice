"""
TITLE: 숫자 맞추기 업다운 게임
DIFFICULTY: medium
TAGS: while, if, elif, break

DESCRIPTION:
정답은 `42`로 고정되어 있습니다. 사용자가 맞출 때까지 숫자를 반복 입력받아
- 입력값이 정답보다 작으면 `UP!`
- 입력값이 정답보다 크면 `DOWN!`
- 정답이면 `정답입니다! 시도 횟수: N번`을 출력하고 종료하시오.

첫 줄에 `=== 숫자 맞추기 게임 (1~100) ===`을 출력한 뒤 게임을 시작합니다.

예시:
- 입력: 50, 25, 37, 42 → DOWN!, UP!, UP!, 정답! (4번)
"""
# META_TESTS:
# - stdin: "50\n25\n37\n42"
#   expected_stdout: "=== 숫자 맞추기 게임 (1~100) ===\nDOWN!\nUP!\nUP!\n정답입니다! 시도 횟수: 4번"
# - stdin: "42"
#   expected_stdout: "=== 숫자 맞추기 게임 (1~100) ===\n정답입니다! 시도 횟수: 1번"
# - stdin: "1\n100\n42"
#   expected_stdout: "=== 숫자 맞추기 게임 (1~100) ===\nUP!\nDOWN!\n정답입니다! 시도 횟수: 3번"

# while True 안에서 guess 입력, tries += 1, 비교/break
answer = 42
tries = 0
print("=== 숫자 맞추기 게임 (1~100) ===")
# TODO
