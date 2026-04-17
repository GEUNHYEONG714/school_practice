"""
TITLE: 수영장 입장
DIFFICULTY: medium
TAGS: if, elif, comparison, arithmetic
EVAL: stdio

DESCRIPTION:
나이와 시간대를 입력받아 수영장 입장 요금을 계산합니다.

기본 요금 (나이 기준):
- 7세 이하: 무료
- 8~13세 (어린이): 3000원
- 14~18세 (청소년): 5000원
- 19세 이상 (성인): 8000원

시간대 할증:
- 오전: 할증 없음
- 오후: 기본 요금의 50% 추가 (무료 대상은 그대로 무료)

출력 형식:
- `나이: N세 | 시간대: X`
- `입장료: X원`

예시:
- 입력: `25\n오전` → 출력: `나이: 25세 | 시간대: 오전\n입장료: 8000원`
- 입력: `10\n오후` → 출력: `나이: 10세 | 시간대: 오후\n입장료: 4500원`
"""
# META_TESTS:
# - stdin: "25\n오전"
#   expected_stdout: "나이: 25세 | 시간대: 오전\n입장료: 8000원"
# - stdin: "10\n오후"
#   expected_stdout: "나이: 10세 | 시간대: 오후\n입장료: 4500원"
# - stdin: "5\n오후"
#   expected_stdout: "나이: 5세 | 시간대: 오후\n입장료: 0원"

# 나이로 기본 요금을 정하고, 오후면 50% 추가
age = int(input())
time_slot = input()
# TODO
