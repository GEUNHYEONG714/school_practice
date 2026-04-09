"""
실습 9 풀이: 비밀번호 확인
"""

password = "python"
chance = 3  # 남은 기회

# 기회가 남아 있는 동안 반복
while chance > 0:
    user_input = input("비밀번호를 입력하세요: ")

    if user_input == password:
        print("로그인 성공!")
        break  # 맞추면 즉시 반복 종료
    else:
        chance -= 1  # 틀리면 기회 1회 차감
        if chance > 0:
            # 아직 기회가 남아 있으면 남은 횟수 안내
            print("틀렸습니다. 남은 기회:", str(chance) + "번")
        else:
            # 기회를 모두 소진하면 잠금
            print("계정이 잠겼습니다")
