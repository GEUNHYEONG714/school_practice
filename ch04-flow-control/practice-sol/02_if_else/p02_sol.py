"""
실습 6 풀이: 가위바위보
"""

computer = "바위"
user = input("가위, 바위, 보 중 하나를 입력하세요: ")

print("컴퓨터:", computer)
print("나:", user)

# 컴퓨터가 "바위"로 고정되어 있으므로
# 사용자 입력에 따라 결과가 결정된다
if user == computer:
    print("결과: 비겼습니다")
elif user == "가위":
    # 가위 vs 바위 → 진다
    print("결과: 졌습니다")
elif user == "보":
    # 보 vs 바위 → 이긴다
    print("결과: 이겼습니다")
else:
    # 가위, 바위, 보 외의 입력 처리
    print("결과: 잘못된 입력입니다")
