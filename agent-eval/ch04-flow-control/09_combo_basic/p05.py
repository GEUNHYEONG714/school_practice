"""
TITLE: 성적 평가 및 수료 판정
DIFFICULTY: medium
TAGS: if, elif, else, nested
EVAL: stdio

DESCRIPTION:
점수(0~100)와 출석률(0~100)을 각각 한 줄씩 정수로 입력받아 등급과 수료 여부를 출력하시오.

등급 기준:
- 90점 이상: A
- 80점 이상: B
- 70점 이상: C
- 60점 이상: D
- 60점 미만: F

출력 형식:
`등급: X`
그리고 다음 중 하나:
- 등급이 F면: `미수료 - 성적 미달 (60점 이상 필요)`
- 등급이 F가 아니고 출석률 < 80이면: `미수료 - 출석률 부족 (80% 이상 필요)`
- 그 외: `수료를 축하합니다!`

예시:
- 입력: `85\n90` → 출력: `등급: B\n수료를 축하합니다!`
"""
# META_TESTS:
# - stdin: "85\n90"
#   expected_stdout: "등급: B\n수료를 축하합니다!"
# - stdin: "75\n60"
#   expected_stdout: "등급: C\n미수료 - 출석률 부족 (80% 이상 필요)"
# - stdin: "40\n95"
#   expected_stdout: "등급: F\n미수료 - 성적 미달 (60점 이상 필요)"

# 먼저 등급을 판별한 뒤 수료 여부를 판단하세요.
score = int(input())
attendance = int(input())
# TODO
