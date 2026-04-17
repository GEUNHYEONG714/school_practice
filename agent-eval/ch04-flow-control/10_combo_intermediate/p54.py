"""
TITLE: 디오판토스 방정식
DIFFICULTY: hard
TAGS: algorithm, math, brute-force, for, if
EVAL: stdio

DESCRIPTION:
세 정수 a, b, c를 한 줄에 공백으로 구분하여 입력받아,
ax + by = c 를 만족하는 음이 아닌 정수 해 (x, y)를 모두 구하시오.
(0 <= x <= 100, 0 <= y <= 100)

각 해를 `x=X, y=Y` 형식으로 한 줄에 하나씩 출력한다.
x 오름차순으로 출력한다.
해가 없으면 `해가 없습니다` 를 출력한다.

예시:
- 입력: `2 3 12` → 2x + 3y = 12의 해 출력
"""
# META_TESTS:
# - stdin: "2 3 12"
#   expected_stdout: "x=0, y=4\nx=3, y=2\nx=6, y=0"
# - stdin: "5 7 1"
#   expected_stdout: "해가 없습니다"
# - stdin: "1 1 3"
#   expected_stdout: "x=0, y=3\nx=1, y=2\nx=2, y=1\nx=3, y=0"

# x를 0부터 100까지 순회하며 (c - a*x)가 b로 나누어 떨어지는지 확인
line = input()
parts = line.split()
a = int(parts[0])
b = int(parts[1])
c = int(parts[2])
# TODO
