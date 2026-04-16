"""
TITLE: 혈액형 성격
DIFFICULTY: easy
TAGS: if, elif, else, string

EVAL: stdio

DESCRIPTION:
혈액형(`A`, `B`, `O`, `AB`)을 입력받아 두 줄로 출력하시오.

```
혈액형: {혈액형}형
성격: {설명}
```

성격 기준:
- A형: 꼼꼼하고 신중한 성격
- B형: 자유롭고 창의적인 성격
- O형: 사교적이고 리더십이 강한 성격
- AB형: 이성적이고 독창적인 성격
- 그 외 입력은 `잘못된 입력입니다.`만 출력

주의: `AB`가 `A`보다 먼저 검사되어야 합니다.

예시:
- 입력: `AB` → 출력: `혈액형: AB형\n성격: 이성적이고 독창적인 성격`
- 입력: `A` → 출력: `혈액형: A형\n성격: 꼼꼼하고 신중한 성격`
- 입력: `X` → 출력: `잘못된 입력입니다.`
"""
# META_TESTS:
# - stdin: "AB"
#   expected_stdout: "혈액형: AB형\n성격: 이성적이고 독창적인 성격"
# - stdin: "A"
#   expected_stdout: "혈액형: A형\n성격: 꼼꼼하고 신중한 성격"
# - stdin: "X"
#   expected_stdout: "잘못된 입력입니다."

# AB형을 A보다 먼저 검사해야 합니다.
blood = input()
# TODO
