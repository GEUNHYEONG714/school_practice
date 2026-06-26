# 문제 2. 같은 코드를 반복해서 작성하게 된다
#
# 학생들의 점수로 학점을 매겨 출력한다.
# "학점을 매기는 규칙"은 학생마다 똑같다.
# 그런데 함수가 없으면 같은 규칙을 학생 수만큼 복사하게 된다.
# 복사한 코드는 길어질 뿐 아니라, 나중에 규칙이 바뀔 때 모두 고쳐야 해서 위험하다.

print("=" * 40)
print("[함수 없이] 같은 코드를 복사-붙여넣기")
print("=" * 40)

# --- 1번 학생 ---
score = 92
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"홍길동: {score}점 → {grade}")

# --- 2번 학생 (위와 똑같은 규칙을 또 복사...) ---
score = 76
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"김철수: {score}점 → {grade}")

# --- 3번 학생 (복사할수록 실수할 곳도 늘어난다) ---
score = 88
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"이영희: {score}점 → {grade}")

# → 학생이 30명이면? 같은 규칙을 30번 복사해야 한다!
# → 학점 기준을 바꾸려면? 복사된 30곳을 빠짐없이 찾아 고쳐야 한다.


print()
print("=" * 40)
print("[함수 사용] 규칙은 '한 번만' 정의한다")
print("=" * 40)

# 학점 매기는 규칙을 함수로 '한 번만' 작성한다.
# 이제 학점 규칙의 진짜 위치는 grade_of() 한 곳이다.
def grade_of(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

# 필요할 때마다 '불러서' 쓰기만 하면 된다.
# 함수 호출 한 줄이 "이 점수의 학점을 구한다"라는 의미를 가진다.
print(f"홍길동: 92점 → {grade_of(92)}")
print(f"김철수: 76점 → {grade_of(76)}")
print(f"이영희: 88점 → {grade_of(88)}")

# 학생이 30명, 300명이어도 점수만 바꿔 grade_of()를 호출하면 된다.
# 규칙이 바뀌면 함수 안만 고치면 되므로, 반복 코드보다 훨씬 안전하다.
students = [("박민준", 95), ("최지우", 67), ("정수빈", 81)]
for name, sc in students:
    print(f"{name}: {sc}점 → {grade_of(sc)}")
