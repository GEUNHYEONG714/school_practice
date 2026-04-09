"""
실습 풀이: 로그인 시스템
"""

user_id = input("아이디를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

# 바깥 if: 아이디 확인
if user_id == "admin":
    # 안쪽 if: 비밀번호 확인 (아이디가 맞을 때만 검사)
    if password == "1234":
        print("로그인 성공!")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("ID가 존재하지 않습니다.")
