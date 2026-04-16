"""
TITLE: 5개 숫자 중 최소값
DIFFICULTY: medium
TAGS: for, if, min
EVAL: stdio

DESCRIPTION:
5개의 정수를 한 줄에 하나씩 입력받아 그 중 최소값을 `최소값: 값` 형식으로 출력하시오.
리스트를 사용하지 말고 변수만으로 해결합니다.

예시:
- 입력: `35\n12\n48\n7\n23` → 출력: `최소값: 7`
"""
# META_TESTS:
# - stdin: "35\n12\n48\n7\n23"
#   expected_stdout: "최소값: 7"
# - stdin: "10\n20\n30\n40\n50"
#   expected_stdout: "최소값: 10"
# - stdin: "-1\n-5\n-3\n0\n2"
#   expected_stdout: "최소값: -5"

# 첫 번째 입력을 minimum으로 두고 나머지와 비교하세요.
# TODO
