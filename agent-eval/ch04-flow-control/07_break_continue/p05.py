"""
TITLE: 특정 문자 찾기
DIFFICULTY: medium
TAGS: for, break, string-index

EVAL: stdio

DESCRIPTION:
문자열은 `hello python`, 찾을 문자는 `p`입니다.
문자열을 앞에서부터 한 글자씩 확인해 처음으로 찾은 위치(인덱스)에서
`'p'을(를) I번째 위치에서 찾았습니다!` 형식으로 출력하고 즉시 종료하시오.
끝까지 찾지 못하면 `찾지 못했습니다`를 출력합니다.

예시:
- 입력: (없음) → 출력: `'p'을(를) 6번째 위치에서 찾았습니다!`
"""
# META_TESTS:
# - stdin: ""
#   expected_stdout: "'p'을(를) 6번째 위치에서 찾았습니다!"

# for i in range(len(text)): 조건 만족 시 출력 후 break. found 플래그로 미발견 처리.
text = "hello python"
target = "p"
# TODO
