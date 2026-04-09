"""
실습 45 풀이: 퀴즈 게임
"""

score = 0

# 문제 1
a1 = 12
b1 = 8
answer1 = 20
print("문제 1:", a1, "+", b1, "= ?")
user1 = int(input("답: "))
if user1 == answer1:
    print("정답!")
    score += 20
else:
    print("오답! 정답은", str(answer1) + "입니다")

# 문제 2
a2 = 35
b2 = 17
answer2 = 52
print("문제 2:", a2, "+", b2, "= ?")
user2 = int(input("답: "))
if user2 == answer2:
    print("정답!")
    score += 20
else:
    print("오답! 정답은", str(answer2) + "입니다")

# 문제 3
a3 = 99
b3 = 1
answer3 = 100
print("문제 3:", a3, "+", b3, "= ?")
user3 = int(input("답: "))
if user3 == answer3:
    print("정답!")
    score += 20
else:
    print("오답! 정답은", str(answer3) + "입니다")

# 문제 4
a4 = 46
b4 = 27
answer4 = 73
print("문제 4:", a4, "+", b4, "= ?")
user4 = int(input("답: "))
if user4 == answer4:
    print("정답!")
    score += 20
else:
    print("오답! 정답은", str(answer4) + "입니다")

# 문제 5
a5 = 58
b5 = 34
answer5 = 92
print("문제 5:", a5, "+", b5, "= ?")
user5 = int(input("답: "))
if user5 == answer5:
    print("정답!")
    score += 20
else:
    print("오답! 정답은", str(answer5) + "입니다")

print("=== 최종 점수:", score, "/ 100 ===")
