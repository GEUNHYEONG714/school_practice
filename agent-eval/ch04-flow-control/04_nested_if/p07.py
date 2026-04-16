"""
TITLE: 영화 추천
DIFFICULTY: easy
TAGS: nested, if, else, string

EVAL: stdio

DESCRIPTION:
장르(`액션` 또는 `로맨스`)와 나이를 순서대로 입력받아 추천 영화를 출력하시오.

- 액션:
  - 19세 이상: `추천: 존 윅`
  - 19세 미만: `추천: 스파이더맨`
- 로맨스:
  - 19세 이상: `추천: 노트북`
  - 19세 미만: `추천: 너의 이름은`
- 그 외 장르: `해당 장르의 추천 영화가 없습니다.`

예시:
- 입력: `액션\n25` → 출력: `추천: 존 윅`
- 입력: `로맨스\n16` → 출력: `추천: 너의 이름은`
- 입력: `공포\n20` → 출력: `해당 장르의 추천 영화가 없습니다.`
"""
# META_TESTS:
# - stdin: "액션\n25"
#   expected_stdout: "추천: 존 윅"
# - stdin: "로맨스\n16"
#   expected_stdout: "추천: 너의 이름은"
# - stdin: "공포\n20"
#   expected_stdout: "해당 장르의 추천 영화가 없습니다."

# 장르 판정 후 나이 판정으로 중첩하세요.
genre = input()
age = int(input())
# TODO
