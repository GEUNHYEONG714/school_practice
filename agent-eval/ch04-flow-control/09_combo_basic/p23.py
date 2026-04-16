"""
TITLE: 합격자 수 세기
DIFFICULTY: medium
TAGS: for, if, counter
EVAL: stdio

DESCRIPTION:
먼저 학생 수 N을 입력받고, 이어서 N명의 점수를 한 줄에 하나씩 입력받아 60점 이상 합격자 수를 출력하시오.

출력 형식: `합격자 수: 값`

예시:
- 입력: `5\n85\n42\n60\n55\n90` → 출력: `합격자 수: 3`
"""
# META_TESTS:
# - stdin: "5\n85\n42\n60\n55\n90"
#   expected_stdout: "합격자 수: 3"
# - stdin: "3\n50\n55\n59"
#   expected_stdout: "합격자 수: 0"
# - stdin: "4\n100\n100\n100\n100"
#   expected_stdout: "합격자 수: 4"

# for + if를 사용하세요.
n = int(input())
count = 0
# TODO

print("합격자 수:", count)
