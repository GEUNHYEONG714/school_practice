"""
실습 8 풀이: 나만의 파스타 만들기
"""

add_cheese = input("치즈를 추가할까요? (예/아니오): ")
add_bacon = input("베이컨을 추가할까요? (예/아니오): ")
add_shrimp = input("새우를 추가할까요? (예/아니오): ")

# 기본 파스타 문자열
pasta = "파스타"

# 각 재료마다 독립적인 단일 if문으로 판단
# "예"라고 답한 재료만 문자열에 이어 붙인다
if add_cheese == "예":
    pasta += " + 치즈"

if add_bacon == "예":
    pasta += " + 베이컨"

if add_shrimp == "예":
    pasta += " + 새우"

# 최종 결과 출력
print("나의 파스타: " + pasta)
