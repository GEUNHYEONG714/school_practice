"""
실습 11 풀이: 눈코딩 - if/elif/else 실행 결과 예측
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
# 정답: C
# 75는 90 미만, 80 미만이지만 70 이상이므로 "C"


# ── 문제 2 ──
num = 0
if num > 0:
    print("양수")
elif num < 0:
    print("음수")
else:
    print("영")
# 정답: 영
# 0은 양수도 음수도 아니므로 else 실행


# ── 문제 3 ──
score = 95
if score >= 60:
    print("합격")
elif score >= 90:
    print("우수")
else:
    print("불합격")
# 정답: 합격
# 95 >= 60이 참이므로 "합격" 출력 후 나머지 elif/else는 건너뜀
# "우수"는 절대 출력되지 않는다 → 조건 순서가 잘못된 코드!
# 올바른 순서: score >= 90을 먼저 검사해야 한다


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
# 정답: 청소년
#        투표 불가
# 15 >= 20은 거짓, 15 >= 14는 참 → "청소년"과 "투표 불가" 출력


# ── 문제 5 ──
temp = 35
if temp >= 30:
    print("더움")
if temp >= 20:
    print("따뜻")
if temp >= 10:
    print("선선")
# 정답: 더움
#        따뜻
#        선선
# if-if-if는 각각 독립적으로 검사한다 → 세 조건 모두 참 → 모두 출력
# elif를 사용했다면 "더움"만 출력되었을 것이다
