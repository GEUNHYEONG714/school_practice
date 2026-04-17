"""
TITLE: 행맨 게임
DIFFICULTY: hard
TAGS: game, string, loop, if, hangman
EVAL: stdio

DESCRIPTION:
정답 단어는 "PYTHON"으로 고정되어 있습니다.
플레이어가 5개의 알파벳을 한 줄에 하나씩 입력합니다 (대문자).
각 입력마다 현재까지 맞춘 글자를 공개하고, 못 맞춘 글자는 _로 표시합니다.
마지막에 "성공" (모든 글자 공개) 또는 "실패"를 출력합니다.
(리스트/딕셔너리/함수 사용 금지, 변수만 사용)

예시:
- 입력: P, Y, T, H, O (각 줄에 하나씩)
- 출력:
  P _ _ _ _ _
  P Y _ _ _ _
  P Y T _ _ _
  P Y T H _ _
  P Y T H O _
  실패

- 입력: P, Y, T, H, N (각 줄에 하나씩)
- 출력:
  P _ _ _ _ _
  P Y _ _ _ _
  P Y T _ _ _
  P Y T H _ _
  P Y T H _ N
  실패
"""
# META_TESTS:
# - stdin: "P\nY\nT\nH\nO"
#   expected_stdout: "P _ _ _ _ _\nP Y _ _ _ _\nP Y T _ _ _\nP Y T H _ _\nP Y T H O _\n실패"
# - stdin: "P\nY\nT\nH\nN"
#   expected_stdout: "P _ _ _ _ _\nP Y _ _ _ _\nP Y T _ _ _\nP Y T H _ _\nP Y T H _ N\n실패"
# - stdin: "A\nB\nC\nD\nE"
#   expected_stdout: "_ _ _ _ _ _\n_ _ _ _ _ _\n_ _ _ _ _ _\n_ _ _ _ _ _\n_ _ _ _ _ _\n실패"

# 행맨 게임: 정답 "PYTHON", 5번의 기회로 글자를 맞추세요.
# TODO
