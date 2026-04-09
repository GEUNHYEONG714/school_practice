"""
실습 51 풀이: 학생 석차
"""

print("=== 5명의 점수 입력 ===")
s1 = int(input("1번 학생 점수: "))
s2 = int(input("2번 학생 점수: "))
s3 = int(input("3번 학생 점수: "))
s4 = int(input("4번 학생 점수: "))
s5 = int(input("5번 학생 점수: "))

target = int(input("석차를 확인할 학생 번호 (1~5): "))

# 선택한 학생의 점수 가져오기
my_score = 0
if target == 1:
    my_score = s1
elif target == 2:
    my_score = s2
elif target == 3:
    my_score = s3
elif target == 4:
    my_score = s4
elif target == 5:
    my_score = s5

# 석차 계산: 나보다 점수가 높은 사람 수 + 1
rank = 1

if s1 > my_score:
    rank += 1
if s2 > my_score:
    rank += 1
if s3 > my_score:
    rank += 1
if s4 > my_score:
    rank += 1
if s5 > my_score:
    rank += 1

print(str(target) + "번 학생 점수:", my_score)
print("석차:", str(rank) + "등")
