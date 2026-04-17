"""
TITLE: 놀이기구 추천
DIFFICULTY: easy-medium
TAGS: if, elif, else, validation, block-scope
EVAL: stdio

DESCRIPTION:
나이를 입력받아 추천 놀이기구를 출력하시오.
- 5세 이하: `회전목마`
- 6~12세: `범퍼카`
- 13~17세: `롤러코스터`
- 18세 이상: `자이로드롭`
- 0 이하(잘못된 입력): `잘못된 입력입니다`

어떤 경우든 마지막에 `즐거운 하루 되세요!`를 출력하시오.

예시:
- 입력: `10` → 출력: `범퍼카\n즐거운 하루 되세요!`
- 입력: `20` → 출력: `자이로드롭\n즐거운 하루 되세요!`
- 입력: `-1` → 출력: `잘못된 입력입니다\n즐거운 하루 되세요!`
"""
# META_TESTS:
# - stdin: "10"
#   expected_stdout: "범퍼카\n즐거운 하루 되세요!"
# - stdin: "20"
#   expected_stdout: "자이로드롭\n즐거운 하루 되세요!"
# - stdin: "-1"
#   expected_stdout: "잘못된 입력입니다\n즐거운 하루 되세요!"
# - stdin: "3"
#   expected_stdout: "회전목마\n즐거운 하루 되세요!"
# - stdin: "15"
#   expected_stdout: "롤러코스터\n즐거운 하루 되세요!"

# 나이를 입력받아 놀이기구를 추천하고, 항상 인사말을 출력하세요.
age = int(input())
# TODO
