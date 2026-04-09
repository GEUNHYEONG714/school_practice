"""
실습 7 풀이: 영화 추천
"""

genre = input("장르를 입력하세요 (액션/로맨스): ")
age = int(input("나이를 입력하세요: "))

# 바깥 if/elif/else: 장르 분기
if genre == "액션":
    # 안쪽 if: 나이에 따라 다른 영화 추천
    if age >= 19:
        print("추천: 존 윅")
    else:
        print("추천: 스파이더맨")
elif genre == "로맨스":
    # 안쪽 if: 나이에 따라 다른 영화 추천
    if age >= 19:
        print("추천: 노트북")
    else:
        print("추천: 너의 이름은")
else:
    print("해당 장르의 추천 영화가 없습니다.")
