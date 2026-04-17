"""
TITLE: 도서 대여료
DIFFICULTY: medium
TAGS: if, arithmetic, comparison
EVAL: stdio

DESCRIPTION:
도서 대여 일수를 입력받아 대여료를 계산합니다.

요금 규칙:
- 7일 이내: 무료 (0원)
- 8일부터: 일당 200원 추가 (초과 일수 × 200)

출력 형식:
- `대여 일수: N일`
- `대여료: X원`

예시:
- 입력: `5` → 출력: `대여 일수: 5일\n대여료: 0원`
- 입력: `10` → 출력: `대여 일수: 10일\n대여료: 600원`
"""
# META_TESTS:
# - stdin: "5"
#   expected_stdout: "대여 일수: 5일\n대여료: 0원"
# - stdin: "10"
#   expected_stdout: "대여 일수: 10일\n대여료: 600원"
# - stdin: "7"
#   expected_stdout: "대여 일수: 7일\n대여료: 0원"

# 7일 초과분에 대해 일당 200원 부과
days = int(input())
# TODO
