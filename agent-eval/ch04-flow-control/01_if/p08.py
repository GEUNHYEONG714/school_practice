"""
TITLE: 나만의 파스타 만들기
DIFFICULTY: easy
TAGS: if, string-concat, input
EVAL: stdio

DESCRIPTION:
파스타 주문 시스템입니다. 기본 `파스타`에 3가지 토핑을 선택적으로 추가합니다.

3개의 입력을 순서대로 받습니다. 각각 `예` 또는 `아니오`입니다.
- 치즈 추가 여부
- 베이컨 추가 여부
- 새우 추가 여부

`예`로 답한 재료만 `+ 재료명` 형식으로 이어 붙여 최종 결과를 `나의 파스타: ...` 형식으로 출력하시오.

힌트: 단일 if문 3개를 연달아 사용합니다(if/else 아님). 문자열 += 연산자를 사용합니다.

예시:
- 입력: `예\n아니오\n예` → 출력: `나의 파스타: 파스타 + 치즈 + 새우`
- 입력: `예\n예\n예` → 출력: `나의 파스타: 파스타 + 치즈 + 베이컨 + 새우`
- 입력: `아니오\n아니오\n아니오` → 출력: `나의 파스타: 파스타`
"""
# META_TESTS:
# - stdin: "예\n아니오\n예"
#   expected_stdout: "나의 파스타: 파스타 + 치즈 + 새우"
# - stdin: "예\n예\n예"
#   expected_stdout: "나의 파스타: 파스타 + 치즈 + 베이컨 + 새우"
# - stdin: "아니오\n아니오\n아니오"
#   expected_stdout: "나의 파스타: 파스타"

# "예"로 답한 재료만 이어 붙여 "나의 파스타: ..." 형식으로 출력하세요.
add_cheese = input()
add_bacon = input()
add_shrimp = input()
pasta = "파스타"
# TODO
