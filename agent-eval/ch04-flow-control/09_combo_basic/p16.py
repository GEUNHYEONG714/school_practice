"""
TITLE: N명 평균 점수
DIFFICULTY: medium
TAGS: for, accumulator
EVAL: stdio

DESCRIPTION:
먼저 학생 수 N을 입력받고, 이어서 N명의 점수를 한 줄에 하나씩 입력받아 평균 점수를 출력하시오.

출력 형식: `평균 점수: 값` (합계 / N, 실수 그대로)

예시:
- 입력: `3\n80\n90\n70` → 출력: `평균 점수: 80.0`
"""
# META_TESTS:
# - stdin: "3\n80\n90\n70"
#   expected_stdout: "평균 점수: 80.0"
# - stdin: "5\n100\n100\n100\n100\n100"
#   expected_stdout: "평균 점수: 100.0"
# - stdin: "2\n50\n75"
#   expected_stdout: "평균 점수: 62.5"

# for + 누적 변수를 사용하세요.
n = int(input())
# TODO
