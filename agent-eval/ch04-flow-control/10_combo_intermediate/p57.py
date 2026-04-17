"""
TITLE: 풍선 터뜨리기 (요세푸스)
DIFFICULTY: hard
TAGS: algorithm, simulation, while, for, if
EVAL: stdio

DESCRIPTION:
두 정수 N과 K를 한 줄에 공백으로 구분하여 입력받으시오.
N개의 풍선이 원형으로 1번부터 N번까지 배치되어 있다.

1번 풍선부터 시작하여 K번째 풍선을 터뜨리는 것을 반복한다.
터뜨린 풍선은 건너뛰고 다음 남은 풍선부터 다시 센다.
모든 풍선이 터질 때까지 반복한다.

터뜨린 순서를 한 줄에 공백으로 구분하여 출력한다.

리스트를 사용하지 않고, 각 풍선의 생존 여부를 개별 변수나
숫자 비트 연산 등으로 관리한다. (N은 최대 10)

예시:
- 입력: `5 2` → 2 4 1 5 3
"""
# META_TESTS:
# - stdin: "5 2"
#   expected_stdout: "2 4 1 5 3"
# - stdin: "7 3"
#   expected_stdout: "3 6 2 7 5 1 4"
# - stdin: "4 1"
#   expected_stdout: "1 2 3 4"

# 비트마스크로 풍선 생존 관리: alive 변수의 각 비트가 풍선 상태
line = input()
parts = line.split()
n = int(parts[0])
k = int(parts[1])
# TODO
