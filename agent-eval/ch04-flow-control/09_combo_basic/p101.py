"""
TITLE: 단어 검열기
DIFFICULTY: medium
TAGS: for, if, string, combo
EVAL: stdio

DESCRIPTION:
문장과 금지어를 입력받아, 문장에서 금지어를 ***로 대체하여 출력하시오.

첫째 줄: 원본 문장
둘째 줄: 금지어

금지어가 문장에 여러 번 등장하면 모두 ***로 대체합니다.
대소문자를 구분합니다.

for문으로 문장을 순회하며 금지어를 찾아 대체하세요.
(replace 메서드 대신 직접 구현)

출력: 검열된 문장

예시:
- 입력: `나는 바보라서 바보같은 실수를 했다`, `바보`
  → 출력: `나는 ***라서 ***같은 실수를 했다`
"""
# META_TESTS:
# - stdin: "나는 바보라서 바보같은 실수를 했다\n바보"
#   expected_stdout: "나는 ***라서 ***같은 실수를 했다"
# - stdin: "hello world hello\nhello"
#   expected_stdout: "*** world ***"
# - stdin: "아무 문제 없는 문장입니다\n금지"
#   expected_stdout: "아무 문제 없는 문장입니다"

# for문과 인덱스를 사용하여 금지어를 찾아 대체하세요.
sentence = input()
banned = input()
# TODO
