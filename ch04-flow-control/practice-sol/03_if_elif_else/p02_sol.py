"""
실습 2 풀이: 계절 판별
"""

month = int(input("월을 입력하세요 (1~12): "))

# 3~5월은 봄, 6~8월은 여름, 9~11월은 가을, 나머지는 겨울
if 3 <= month <= 5:
    season = "봄"
elif 6 <= month <= 8:
    season = "여름"
elif 9 <= month <= 11:
    season = "가을"
else:
    season = "겨울"

print(str(month) + "월은 " + season + "입니다.")
