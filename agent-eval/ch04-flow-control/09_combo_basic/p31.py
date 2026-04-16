"""
TITLE: 구간 반복 합계
DIFFICULTY: medium
TAGS: for, if, range

DESCRIPTION:
시작값과 끝값을 한 줄에 하나씩 입력받아 그 구간[start, end]의 전체 합계와
짝수의 합을 구해 다음 형식으로 출력하시오.
`구간 합계: T`
`짝수 합계: E`

예시:
- 입력: 1, 10 → 구간 합계 55, 짝수 합계 30
"""
# META_TESTS:
# - stdin: "1\n10"
#   expected_stdout: "구간 합계: 55\n짝수 합계: 30"
# - stdin: "3\n7"
#   expected_stdout: "구간 합계: 25\n짝수 합계: 10"

# range(start, end+1)로 반복
start = int(input())
end = int(input())
total = 0
even_sum = 0
# TODO
print("구간 합계:", total)
print("짝수 합계:", even_sum)
