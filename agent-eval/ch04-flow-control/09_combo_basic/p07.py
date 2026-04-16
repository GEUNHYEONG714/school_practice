"""
TITLE: BMI 판정
DIFFICULTY: medium
TAGS: if, elif, else, nested, arithmetic
EVAL: stdio

DESCRIPTION:
키(cm, 실수), 몸무게(kg, 실수), 나이(정수)를 각각 한 줄씩 입력받아 BMI를 계산하고 판정을 출력하시오.

BMI = weight / ((height/100) ** 2). BMI는 `round(bmi, 2)`로 출력합니다.

성인(age >= 20):
- < 18.5: `판정: 저체중`
- < 23: `판정: 정상`
- < 25: `판정: 과체중`
- 그 외: `판정: 비만`

청소년(age < 20):
- < 17: `판정: 저체중 (청소년 기준)`
- < 23: `판정: 정상 (청소년 기준)`
- 그 외: `판정: 과체중 주의 (청소년 기준)`

출력 형식:
`BMI: 값`
`판정: 값`

예시:
- 입력: `175\n70\n25` → 출력: `BMI: 22.86\n판정: 정상`
"""
# META_TESTS:
# - stdin: "175\n70\n25"
#   expected_stdout: "BMI: 22.86\n판정: 정상"
# - stdin: "165\n50\n16"
#   expected_stdout: "BMI: 18.37\n판정: 정상 (청소년 기준)"
# - stdin: "170\n80\n30"
#   expected_stdout: "BMI: 27.68\n판정: 비만"

# 나이로 기준을 먼저 나누세요.
height = float(input())
weight = float(input())
age = int(input())
# TODO
