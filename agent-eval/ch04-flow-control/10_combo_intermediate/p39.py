"""
TITLE: 온도 조절기
DIFFICULTY: hard
TAGS: simulation, while, if
EVAL: stdio

DESCRIPTION:
현재 온도와 목표 온도를 받아 1도씩 변경 과정을 출력하시오.
- 현재 온도 == 목표 온도: `이미 목표 온도입니다.` 출력 후 종료
- 현재 온도 < 목표 온도: `난방 모드를 시작합니다.` 출력 후 1도씩 올리며 `현재 온도: X도 → Y도`, 도달 시 `목표 온도 T도에 도달했습니다!`
- 현재 온도 > 목표 온도: `냉방 모드를 시작합니다.` 출력 후 1도씩 내리며 위와 유사

입력 형식: 현재 온도, 목표 온도 (각 줄)
"""
# META_TESTS:
# - stdin: "18\n22"
#   expected_stdout: "난방 모드를 시작합니다.\n현재 온도: 18도 → 19도\n현재 온도: 19도 → 20도\n현재 온도: 20도 → 21도\n현재 온도: 21도 → 22도\n목표 온도 22도에 도달했습니다!"
# - stdin: "26\n24"
#   expected_stdout: "냉방 모드를 시작합니다.\n현재 온도: 26도 → 25도\n현재 온도: 25도 → 24도\n목표 온도 24도에 도달했습니다!"
# - stdin: "22\n22"
#   expected_stdout: "이미 목표 온도입니다."

# if/elif로 모드 분기 후 while로 변경 과정 출력
current_temp = int(input())
target_temp = int(input())
# TODO
