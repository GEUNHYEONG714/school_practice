"""
TITLE: 택배 요금
DIFFICULTY: medium
TAGS: if, elif, arithmetic, comparison
EVAL: stdio

DESCRIPTION:
택배 무게(kg)와 거리(km)를 입력받아 택배 요금을 계산합니다.

기본료: 3000원

무게 추가:
- 2kg 이하: 추가 없음
- 2kg 초과 ~ 10kg 이하: 1000원 추가
- 10kg 초과: 3000원 추가

거리 추가:
- 50km 이하: 추가 없음
- 50km 초과 ~ 100km 이하: 1500원 추가
- 100km 초과: 3000원 추가

출력 형식:
- `무게: Nkg | 거리: Mkm`
- `택배 요금: X원`

예시:
- 입력: `1\n30` → 출력: `무게: 1kg | 거리: 30km\n택배 요금: 3000원`
- 입력: `5\n80` → 출력: `무게: 5kg | 거리: 80km\n택배 요금: 5500원`
"""
# META_TESTS:
# - stdin: "1\n30"
#   expected_stdout: "무게: 1kg | 거리: 30km\n택배 요금: 3000원"
# - stdin: "5\n80"
#   expected_stdout: "무게: 5kg | 거리: 80km\n택배 요금: 5500원"
# - stdin: "15\n150"
#   expected_stdout: "무게: 15kg | 거리: 150km\n택배 요금: 9000원"

# 기본료에 무게 추가, 거리 추가를 더하세요
weight = int(input())
dist = int(input())
# TODO
