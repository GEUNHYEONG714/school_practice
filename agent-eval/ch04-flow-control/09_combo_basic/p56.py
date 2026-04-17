"""
TITLE: 주사위 합 판정
DIFFICULTY: medium
TAGS: if, elif, comparison, arithmetic
EVAL: stdio

DESCRIPTION:
두 주사위의 값을 입력받아 결과를 판정합니다.

판정 규칙 (우선순위 순):
- 합이 7이면: `럭키세븐!`
- 두 값이 같으면(더블): `더블!`
- 그 외: `합: X`

출력 형식:
- `주사위: A, B`
- 판정 결과

예시:
- 입력: `3\n4` → 출력: `주사위: 3, 4\n럭키세븐!`
- 입력: `5\n5` → 출력: `주사위: 5, 5\n더블!`
"""
# META_TESTS:
# - stdin: "3\n4"
#   expected_stdout: "주사위: 3, 4\n럭키세븐!"
# - stdin: "5\n5"
#   expected_stdout: "주사위: 5, 5\n더블!"
# - stdin: "2\n3"
#   expected_stdout: "주사위: 2, 3\n합: 5"

# 합이 7인지, 더블인지 순서대로 확인
d1 = int(input())
d2 = int(input())
# TODO
