"""
TITLE: 곱셈표
DIFFICULTY: medium
TAGS: nested-loop, for, multiplication, table

DESCRIPTION:
크기 N을 입력받아, 1부터 N까지의 곱셈표를 표 형태로 출력하시오.
- 첫 줄에는 헤더 `X\\t1\\t2\\t...\\tN`을 출력합니다.
- 둘째 줄에는 구분선으로 `-`를 30개 출력합니다.
- 이후 각 행(i=1..N)에는 행 번호 `i`에 이어서 `i*1, i*2, ..., i*N` 값을
  탭(`\\t`)으로 구분해 출력합니다.
- 모든 값 끝에 탭이 붙는 형식입니다 (`print(값, end="\\t")`).

예시:
- 입력: `3` → 헤더/구분선/3행 출력
"""
# META_TESTS:
# - stdin: "3"
#   expected_stdout: "X\t1\t2\t3\t\n------------------------------\n1\t1\t2\t3\t\n2\t2\t4\t6\t\n3\t3\t6\t9\t"
# - stdin: "2"
#   expected_stdout: "X\t1\t2\t\n------------------------------\n1\t1\t2\t\n2\t2\t4\t"

# print(값, end="\t")로 탭 구분 출력을 만드세요.
n = int(input())
# TODO
