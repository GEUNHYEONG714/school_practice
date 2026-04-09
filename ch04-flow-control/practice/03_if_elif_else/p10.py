"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 10: 눈코딩 - if/elif/else 실행 결과 예측

아래 각 코드의 실행 결과를 예측하여 주석에 적으세요.
직접 실행하지 말고 먼저 머릿속으로 풀어보세요!

핵심 포인트:
- elif는 위에서부터 순서대로 검사한다
- 하나의 조건이 참이면 나머지는 건너뛴다
- else는 모든 조건이 거짓일 때 실행된다
"""

# ── 문제 1 ──
x = 75
if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
else:
    print("D")
# 예측: ______


# ── 문제 2 ──
num = 0
if num > 0:
    print("양수")
elif num < 0:
    print("음수")
else:
    print("영")
# 예측: ______


# ── 문제 3 ──
# 주의: elif는 앞의 조건이 참이면 실행되지 않는다
score = 95
if score >= 60:
    print("합격")
elif score >= 90:
    print("우수")
else:
    print("불합격")
# 예측: ______
# 생각해보기: "우수"가 출력될까요? 왜 그런가요?


# ── 문제 4 ──
age = 15
if age >= 20:
    print("성인")
    print("투표 가능")
elif age >= 14:
    print("청소년")
    print("투표 불가")
else:
    print("어린이")
    print("투표 불가")
# 예측: ______
#        ______


# ── 문제 5 ──
# 주의: if-elif-else vs 여러 개의 if
temp = 35
if temp >= 30:
    print("더움")
if temp >= 20:
    print("따뜻")
if temp >= 10:
    print("선선")
# 예측: ______
# 생각해보기: elif를 사용했다면 결과가 어떻게 달라질까요?


"""
[정답은 p10_sol.py를 확인하세요]
"""
