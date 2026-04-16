"""
TITLE: 회문 판별
DIFFICULTY: medium
TAGS: for, range, if, string

DESCRIPTION:
문자열을 입력받아 회문(앞뒤가 같은 단어)인지 판별하시오.
회문이면 `TEXT은(는) 회문입니다!`, 아니면 `TEXT은(는) 회문이 아닙니다.`를 출력하시오.

예시:
- 입력: `level` → 출력: `level은(는) 회문입니다!`
- 입력: `hello` → 출력: `hello은(는) 회문이 아닙니다.`
"""
# META_TESTS:
# - stdin: "level"
#   expected_stdout: "level은(는) 회문입니다!"
# - stdin: "hello"
#   expected_stdout: "hello은(는) 회문이 아닙니다."
# - stdin: "noon"
#   expected_stdout: "noon은(는) 회문입니다!"

# 뒤집은 문자열과 원본을 비교
text = input()
reversed_text = ""
# TODO
