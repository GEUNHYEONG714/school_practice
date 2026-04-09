"""
실습 4 풀이: 배송 방식
"""

weight = float(input("무게를 입력하세요(kg): "))

# 바깥 if: 무게에 따라 배송 종류가 달라진다
if weight >= 2:
    # 2kg 이상: 택배
    fast = input("빠른 배송을 원하시나요? (Y/N): ")
    if fast == "Y":
        print("택배(빠른 배송) - 5000원")
    else:
        print("택배(일반 배송) - 3000원")
else:
    # 2kg 미만: 우편
    registered = input("등기 우편을 원하시나요? (Y/N): ")
    if registered == "Y":
        print("우편(등기) - 2000원")
    else:
        print("우편(일반) - 1000원")
