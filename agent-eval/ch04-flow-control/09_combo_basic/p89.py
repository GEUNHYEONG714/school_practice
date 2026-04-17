"""
TITLE: 숫자 야구 (간단)
DIFFICULTY: hard
TAGS: while, if, elif, input, comparison, break
EVAL: stdio

DESCRIPTION:
2자리 정답이 37로 고정되어 있습니다.
사용자가 2자리 숫자를 입력하면 스트라이크/볼을 판정합니다.
정답을 맞출 때까지 반복합니다.

판정 규칙:
- 스트라이크: 같은 자리에 같은 숫자
- 볼: 다른 자리에 같은 숫자
- 둘 다 0이면: `아웃`

출력 형식:
- 맞출 때까지: `S스트라이크 B볼` 또는 `아웃`
- 맞추면: `정답! N번 만에 맞춤`

예시:
- 입력: `73\n37` → `0스트라이크 2볼\n정답! 2번 만에 맞춤`
"""
# META_TESTS:
# - stdin: "37"
#   expected_stdout: "정답! 1번 만에 맞춤"
# - stdin: "73\n37"
#   expected_stdout: "0스트라이크 2볼\n정답! 2번 만에 맞춤"
# - stdin: "12\n73\n37"
#   expected_stdout: "아웃\n0스트라이크 2볼\n정답! 3번 만에 맞춤"

# 정답 37을 맞추는 숫자 야구 게임
# TODO
