"""
실습 3 풀이: 할인 적용
"""

is_member = input("회원이신가요? (Y/N): ")

# 바깥 if: 회원 여부 확인
if is_member == "Y":
    # 회원일 때만 VIP 여부를 물어본다
    is_vip = input("VIP 회원이신가요? (Y/N): ")
    # 안쪽 if: VIP 여부에 따라 할인율 다름
    if is_vip == "Y":
        print("20% 할인 적용")
    else:
        print("10% 할인 적용")
else:
    print("할인 없음")
