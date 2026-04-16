"""
TITLE: 배송 방식
DIFFICULTY: easy
TAGS: nested, if, else, float

EVAL: stdio

DESCRIPTION:
무게(kg, 실수)를 입력받고, 이어서 옵션(`Y`/`N`)을 입력받아 배송 방식과 요금을 출력하시오.

- 무게 2kg 이상:
  - 빠른 배송 `Y`: `택배(빠른 배송) - 5000원`
  - 일반 `N`: `택배(일반 배송) - 3000원`
- 무게 2kg 미만:
  - 등기 `Y`: `우편(등기) - 2000원`
  - 일반 `N`: `우편(일반) - 1000원`

예시:
- 입력: `3.5\nY` → 출력: `택배(빠른 배송) - 5000원`
- 입력: `3.5\nN` → 출력: `택배(일반 배송) - 3000원`
- 입력: `0.5\nY` → 출력: `우편(등기) - 2000원`
- 입력: `0.5\nN` → 출력: `우편(일반) - 1000원`
"""
# META_TESTS:
# - stdin: "3.5\nY"
#   expected_stdout: "택배(빠른 배송) - 5000원"
# - stdin: "3.5\nN"
#   expected_stdout: "택배(일반 배송) - 3000원"
# - stdin: "0.5\nY"
#   expected_stdout: "우편(등기) - 2000원"
# - stdin: "0.5\nN"
#   expected_stdout: "우편(일반) - 1000원"

# 무게 판정 → 옵션 입력 → 최종 배송 방식 출력.
weight = float(input())
option = input()
# TODO
