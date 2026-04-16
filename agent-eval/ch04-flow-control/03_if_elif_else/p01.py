"""
TITLE: 성적 등급
DIFFICULTY: easy
TAGS: if, elif, else, comparison

EVAL: stdio

DESCRIPTION:
점수를 입력받아 다음 기준의 등급을 두 줄로 출력하시오.

```
점수: {점수}
등급: {등급}
```

등급 기준:
- 90 이상: A
- 80 이상: B
- 70 이상: C
- 60 이상: D
- 60 미만: F

예시:
- 입력: `85` → 출력: `점수: 85\n등급: B`
- 입력: `100` → 출력: `점수: 100\n등급: A`
- 입력: `55` → 출력: `점수: 55\n등급: F`
"""
# META_TESTS:
# - stdin: "85"
#   expected_stdout: "점수: 85\n등급: B"
# - stdin: "100"
#   expected_stdout: "점수: 100\n등급: A"
# - stdin: "55"
#   expected_stdout: "점수: 55\n등급: F"

# if/elif/else로 등급을 판정하세요.
score = int(input())
# TODO
