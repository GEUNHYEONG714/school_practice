"""
실습 10 풀이: 혈액형 성격
"""

blood = input("혈액형을 입력하세요 (A/B/O/AB): ")

# AB를 먼저 검사해야 한다
# 만약 A를 먼저 검사하면 "AB" 입력 시에도 A로 판정될 수 있다
# (== 비교에서는 사실 문제없지만, in 등을 쓸 때 주의 필요)
if blood == "AB":
    personality = "이성적이고 독창적인 성격"
elif blood == "A":
    personality = "꼼꼼하고 신중한 성격"
elif blood == "B":
    personality = "자유롭고 창의적인 성격"
elif blood == "O":
    personality = "사교적이고 리더십이 강한 성격"
else:
    personality = ""

if personality != "":
    print("혈액형: " + blood + "형")
    print("성격: " + personality)
else:
    print("잘못된 입력입니다.")
