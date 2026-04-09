"""
실습 5 풀이: 비밀번호 확인
"""

password = "python123"
user_input = input("비밀번호를 입력하세요: ")

# 입력값과 저장된 비밀번호를 == 로 비교
if user_input == password:
    print("로그인 성공")
else:
    # else 블록 안에 여러 줄을 쓸 수 있다
    print("비밀번호 오류")
    print("다시 시도하세요")
