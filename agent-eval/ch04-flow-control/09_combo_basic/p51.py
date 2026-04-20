"""
TITLE: 학생 석차
DIFFICULTY: medium
TAGS: if, elif, comparison

DESCRIPTION:
5명의 점수를 한 줄에 하나씩 차례로 입력받아 s1~s5에 저장하고,
6번째 줄에 석차를 확인할 학생 번호(1~5)를 입력받는다.
해당 학생보다 점수가 높은 사람 수 + 1이 석차이다.

출력 형식:
- 첫 줄: `=== 5명의 점수 입력 ===`
- `T번 학생 점수: score`
- `석차: R등`

예시:
- 입력: 85, 92, 78, 95, 88, 1 → 1번 학생은 4등
"""
# META_TESTS:
# - stdin: "85\n92\n78\n95\n88\n1"
#   expected_stdout: "=== 5명의 점수 입력 ===\n1번 학생 점수: 85\n석차: 4등"
# - stdin: "85\n92\n78\n95\n88\n4"
#   expected_stdout: "=== 5명의 점수 입력 ===\n4번 학생 점수: 95\n석차: 1등"
# - stdin: "50\n50\n50\n50\n50\n3"
#   expected_stdout: "=== 5명의 점수 입력 ===\n3번 학생 점수: 50\n석차: 1등"

# 각 학생 점수 입력 후 target 점수를 고르고 더 높은 수 세기
print("=== 5명의 점수 입력 ===")
s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())
target = int(input())
# TODO
