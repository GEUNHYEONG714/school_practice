"""
실습 풀이: 놀이기구 탑승
"""

height = int(input("키를 입력하세요(cm): "))

# 바깥 if: 최소 키 130cm 확인
if height >= 130:
    guardian = input("보호자가 동반하나요? (Y/N): ")
    if guardian == "Y":
        # 보호자 있으면 바로 탑승 가능
        print("보호자와 함께 탑승 가능합니다.")
    else:
        # 보호자 없으면 키 150cm 이상이어야 혼자 탑승 가능
        if height >= 150:
            print("혼자 탑승 가능합니다.")
        else:
            print("보호자가 필요합니다.")
else:
    print("탑승할 수 없습니다.")
