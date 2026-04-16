"""
TITLE: 교통수단 추천
DIFFICULTY: easy
TAGS: if, elif, else, comparison, float

EVAL: stdio

DESCRIPTION:
거리(km, 실수)를 입력받아 두 줄로 출력하시오.

```
거리: {거리}km
추천 교통수단: {교통수단}
```

추천 기준:
- 2km 미만: 도보
- 2km 이상 5km 미만: 자전거
- 5km 이상 20km 미만: 버스
- 20km 이상: 지하철

예시:
- 입력: `8.5` → 출력: `거리: 8.5km\n추천 교통수단: 버스`
- 입력: `1.5` → 출력: `거리: 1.5km\n추천 교통수단: 도보`
- 입력: `25.0` → 출력: `거리: 25.0km\n추천 교통수단: 지하철`
"""
# META_TESTS:
# - stdin: "8.5"
#   expected_stdout: "거리: 8.5km\n추천 교통수단: 버스"
# - stdin: "1.5"
#   expected_stdout: "거리: 1.5km\n추천 교통수단: 도보"
# - stdin: "25.0"
#   expected_stdout: "거리: 25.0km\n추천 교통수단: 지하철"

# float로 입력받아 구간별로 판정하세요.
distance = float(input())
# TODO
