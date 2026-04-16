"""
TITLE: 가위바위보 (컴퓨터 바위 고정)
DIFFICULTY: medium
TAGS: if, elif, else, and, or
EVAL: stdio

DESCRIPTION:
사용자의 선택(1=가위, 2=바위, 3=보)을 정수로 입력받습니다. 컴퓨터는 항상 2(바위)를 냅니다.

- user < 1 또는 user > 3이면 `잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.` 한 줄만 출력.
- 그 외에는 다음 두 줄을 출력:
  첫 줄: `당신: X / 컴퓨터: 바위` (X는 가위/바위/보)
  두 번째 줄:
    - user == 2: `무승부입니다! 😐`
    - user == 3: `축하합니다! 당신이 이겼습니다! 🎉`
    - user == 1: `아쉽게도 졌습니다. 😢`

예시:
- 입력: `3` → 출력: `당신: 보 / 컴퓨터: 바위\n축하합니다! 당신이 이겼습니다! 🎉`
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "당신: 보 / 컴퓨터: 바위\n축하합니다! 당신이 이겼습니다! 🎉"
# - stdin: "2"
#   expected_stdout: "당신: 바위 / 컴퓨터: 바위\n무승부입니다! 😐"
# - stdin: "1"
#   expected_stdout: "당신: 가위 / 컴퓨터: 바위\n아쉽게도 졌습니다. 😢"
# - stdin: "5"
#   expected_stdout: "잘못된 입력입니다. 1, 2, 3 중에서 선택하세요."

# 유효성 검사 후 이름 변환과 승패 판정을 수행하세요.
user = int(input())
computer = 2
# TODO
