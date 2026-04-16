"""
TITLE: 자리 배치
DIFFICULTY: hard
TAGS: nested_loop, simulation
EVAL: stdio

DESCRIPTION:
N명의 인원을 M열로 배치한 결과를 출력하시오.
- 첫 줄에 인원 수 N, 둘째 줄에 열 수 M을 입력
- 좌석 번호는 `행-열` 형태
- 각 행은 `[R행] R-1  R-2  R-3` (좌석 사이는 공백 두 개)
- 마지막 줄에 `총 X행 배치 완료 (N명)`
- 총 행 = N // M (나머지가 있으면 +1)

예시:
- 입력: `8\\n3` → 출력 첫 줄 `[1행] 1-1  1-2  1-3`, 셋째 줄 `[3행] 3-1  3-2`
"""
# META_TESTS:
# - stdin: "8\n3"
#   expected_stdout: "[1행] 1-1  1-2  1-3\n[2행] 2-1  2-2  2-3\n[3행] 3-1  3-2\n총 3행 배치 완료 (8명)"
# - stdin: "6\n3"
#   expected_stdout: "[1행] 1-1  1-2  1-3\n[2행] 2-1  2-2  2-3\n총 2행 배치 완료 (6명)"
# - stdin: "3\n3"
#   expected_stdout: "[1행] 1-1  1-2  1-3\n총 1행 배치 완료 (3명)"

# 이중 반복문과 배치 카운트로 구현하세요.
n = int(input())
m = int(input())
# TODO
