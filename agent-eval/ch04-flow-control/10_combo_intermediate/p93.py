"""
TITLE: 카드 게임 (블랙잭 간소)
DIFFICULTY: hard
TAGS: game, blackjack, loop, if, combination
EVAL: stdio

DESCRIPTION:
카드 3장의 값을 한 줄에 공백으로 구분하여 입력받습니다 (1~11 사이 정수).
3장 중 1장, 2장, 3장 조합의 합을 모두 구하여
21 이하이면서 21에 가장 가까운 합을 출력합니다.
만약 어떤 조합도 21을 넘지 않으면 가장 큰 합을 출력합니다.
모든 단일 카드, 2장 조합, 3장 조합을 고려합니다.
(리스트/딕셔너리/함수 사용 금지, 변수만 사용)

예시:
- 입력: `10 9 3` → 조합: 10,9,3,19,13,12,22 → 21이하 최대=19 → 출력: `19`
- 입력: `7 7 7` → 조합: 7,7,7,14,14,14,21 → 출력: `21`
"""
# META_TESTS:
# - stdin: "10 9 3"
#   expected_stdout: "19"
# - stdin: "7 7 7"
#   expected_stdout: "21"
# - stdin: "1 2 3"
#   expected_stdout: "6"

# 블랙잭 간소: 카드 3장 조합 중 21 이하 최대 합을 구하세요.
line = input().split()
a, b, c = int(line[0]), int(line[1]), int(line[2])
# TODO
