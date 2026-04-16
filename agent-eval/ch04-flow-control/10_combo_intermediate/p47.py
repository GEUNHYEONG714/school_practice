"""
TITLE: 타자 연습
DIFFICULTY: hard
TAGS: string, simulation, while
EVAL: stdio

DESCRIPTION:
세 개의 고정 문장에 대해 타자 연습을 수행하시오.
- 문장: `Hello Python`, `I love coding`, `Practice makes perfect`
- 각 라운드마다 해당 문장을 표시하고 사용자 입력을 받아 글자별 비교
- 정확도 = (맞은 글자 수 / 원본 글자 수) * 100, 소수점 첫째 자리까지 (`int(acc*10)/10`으로 계산)
- 두 문장 길이가 다르면 짧은 쪽만 비교, 길이 차이는 오류로 처리(비교 안 됨)

시작 시 출력 (3줄):
```
=== 타자 연습 ===
표시된 문장을 정확히 입력하세요!

```
(세 번째 줄은 빈 줄)

각 라운드:
```
[N번 문장] 원본문장
정확도: A.A% (C/O 글자)

```
(라운드 끝마다 빈 줄 하나)

마지막에:
```
=== 최종 결과 ===
전체 정확도: A.A% (C/T 글자)
```
"""
# META_TESTS:
# - stdin: "Hello Python\nI love coding\nPractice makes perfect"
#   expected_stdout: "=== 타자 연습 ===\n표시된 문장을 정확히 입력하세요!\n\n[1번 문장] Hello Python\n정확도: 100.0% (12/12 글자)\n\n[2번 문장] I love coding\n정확도: 100.0% (13/13 글자)\n\n[3번 문장] Practice makes perfect\n정확도: 100.0% (22/22 글자)\n\n=== 최종 결과 ===\n전체 정확도: 100.0% (47/47 글자)"

# 3개 문장을 라운드별로 처리하세요.
text1 = "Hello Python"
text2 = "I love coding"
text3 = "Practice makes perfect"
total_correct = 0
total_chars = 0
round_num = 1
# TODO
