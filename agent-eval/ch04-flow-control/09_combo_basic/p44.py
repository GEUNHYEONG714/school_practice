"""
TITLE: 출석부
DIFFICULTY: medium
TAGS: for, if, else

DESCRIPTION:
첫 줄에 학생 수 N을 입력받고, 이후 각 학생마다
첫 줄에 이름, 둘째 줄에 출석 여부(1: 출석, 0: 결석)를 입력받는다.
각 학생에 대해 `이름 - 출석` 또는 `이름 - 결석`을 출력하고,
마지막에 다음 형식으로 출석 결과를 출력하시오.
`--- 출석 결과 ---`
`출석: P 명`
`결석: A 명`

예시:
- 입력: N=2, (김민수, 1), (이영희, 0)
- 출력: `김민수 - 출석`, `이영희 - 결석`, `--- 출석 결과 ---`, `출석: 1 명`, `결석: 1 명`
"""
# META_TESTS:
# - stdin: "2\n김민수\n1\n이영희\n0"
#   expected_stdout: "김민수 - 출석\n이영희 - 결석\n--- 출석 결과 ---\n출석: 1 명\n결석: 1 명"
# - stdin: "3\nA\n1\nB\n1\nC\n0"
#   expected_stdout: "A - 출석\nB - 출석\nC - 결석\n--- 출석 결과 ---\n출석: 2 명\n결석: 1 명"

# N명에 대해 이름, 상태를 반복 입력받아 분류
n = int(input())
present = 0
absent = 0
# TODO
print("--- 출석 결과 ---")
print("출석:", present, "명")
print("결석:", absent, "명")
