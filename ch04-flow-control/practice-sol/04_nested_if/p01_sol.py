"""
실습 1 풀이: 입장 판정
"""

age = int(input("나이를 입력하세요: "))
ticket = input("티켓이 있나요? (Y/N): ")

# 바깥 if: 나이 확인
if age >= 18:
    # 안쪽 if: 티켓 확인
    if ticket == "Y":
        print("입장 가능합니다.")
    else:
        print("티켓을 구매해주세요.")
else:
    print("18세 미만은 입장할 수 없습니다.")
