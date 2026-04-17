"""
TITLE: 학점 계산기 (가중 평균)
DIFFICULTY: hard
TAGS: simulation, gpa, weighted-average, for, if
EVAL: stdio

DESCRIPTION:
N과목의 학점과 이수학점을 입력받아 GPA를 계산하세요.
- 첫 줄에 과목 수 N을 입력받습니다.
- 이후 N줄에 학점(A+, A, B+, B, C+, C, D+, D, F)과 이수학점(정수)을
  공백으로 구분하여 입력받습니다.
- 학점별 점수: A+=4.5, A=4.0, B+=3.5, B=3.0, C+=2.5, C=2.0, D+=1.5, D=1.0, F=0.0
- GPA = (각 과목의 학점점수 * 이수학점)의 합 / 총 이수학점
- 각 과목별로 `과목X: 학점 (이수학점학점)` 형식으로 출력합니다.
- 마지막에 `GPA: X.XX`를 출력합니다 (소수점 둘째 자리).
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시:
- 입력: `3`, `A+ 3`, `B 2`, `A 3` → 출력:
```
과목1: A+ (3학점)
과목2: B (2학점)
과목3: A (3학점)
GPA: 4.06
```
"""
# META_TESTS:
# - stdin: "3\nA+ 3\nB 2\nA 3"
#   expected_stdout: "과목1: A+ (3학점)\n과목2: B (2학점)\n과목3: A (3학점)\nGPA: 4.06"
# - stdin: "2\nF 3\nA+ 3"
#   expected_stdout: "과목1: F (3학점)\n과목2: A+ (3학점)\nGPA: 2.25"
# - stdin: "1\nC+ 2"
#   expected_stdout: "과목1: C+ (2학점)\nGPA: 2.50"

# N과목의 학점과 이수학점을 입력받아 GPA를 계산하세요.
n = int(input())
# TODO
