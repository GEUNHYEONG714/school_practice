"""
TITLE: 놀이공원 입장료
DIFFICULTY: medium
TAGS: if, elif, else, arithmetic
EVAL: stdio

DESCRIPTION:
나이(정수)와 인원 수(정수)를 각각 한 줄씩 입력받아 입장료를 계산하시오.

기본 입장료:
- age <= 3: 0원
- age <= 12: 15000원
- age <= 18: 20000원
- age <= 64: 30000원
- 그 외: 10000원

인원 수가 10명 이상이면 20% 할인: `price = int(price * 0.8)`

출력 형식:
`기본 입장료: 값원`
(10명 이상일 때만) `단체 할인 적용 (20%)!` 한 줄, 그리고 `1인 할인가: 값원` 한 줄
`총 입장료: 값원` (= price * group_count)

예시:
- 입력: `10\n5` → 출력: `기본 입장료: 15000원\n총 입장료: 75000원`
- 입력: `25\n15` → 출력: `기본 입장료: 30000원\n단체 할인 적용 (20%)!\n1인 할인가: 24000원\n총 입장료: 360000원`
"""
# META_TESTS:
# - stdin: "10\n5"
#   expected_stdout: "기본 입장료: 15000원\n총 입장료: 75000원"
# - stdin: "25\n15"
#   expected_stdout: "기본 입장료: 30000원\n단체 할인 적용 (20%)!\n1인 할인가: 24000원\n총 입장료: 360000원"
# - stdin: "70\n2"
#   expected_stdout: "기본 입장료: 10000원\n총 입장료: 20000원"

# 나이별 요금 결정 후 단체 할인을 판단하세요.
age = int(input())
group_count = int(input())
# TODO
