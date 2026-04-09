"""
실습 3 풀이: 계절별 인사
"""

month = int(input("월을 입력하세요 (1~12): "))

# 월에 따라 계절 판별 후 인사말 출력
if month == 3 or month == 4 or month == 5:
    print("봄입니다.")
    print("따뜻한 봄이에요! 꽃구경 가세요 🌸")
elif month == 6 or month == 7 or month == 8:
    print("여름입니다.")
    print("더운 여름이에요! 시원하게 보내세요 🌊")
elif month == 9 or month == 10 or month == 11:
    print("가을입니다.")
    print("선선한 가을이에요! 단풍 구경 가세요 🍂")
elif month == 12 or month == 1 or month == 2:
    print("겨울입니다.")
    print("추운 겨울이에요! 따뜻하게 입으세요 ⛄")
else:
    # 1~12 이외의 숫자 처리
    print("잘못된 입력입니다.")
