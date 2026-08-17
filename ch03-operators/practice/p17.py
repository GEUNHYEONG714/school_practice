"""
실습 17: 점수 처리 프로그램

국어, 영어, 수학 점수를 입력받아 아래 작업을 수행하세요.

[지시사항]
1. 각 점수를 변수에 저장
2. 다중 대입으로 과목명을 한 줄에 저장
3. total = 0으로 초기화
4. +=를 사용하여 총점 계산
5. 평균 계산 후 출력
"""

# 아래에 코드를 작성하세요
# 과목 종류
sub1, sub2, sub3 = "국어", "영어", "수학"

# 각 점수를 입력받기
lan = int(input("국어 점수: "))
eng = int(input("영어 점수: "))
math = int(input("수학 점수: "))

# 초기화
total = 0

# 총점 계산
total += lan
total += eng
total += math

# 평균 계산
average = total / 3

# 출력
print(f"과목: {sub1} {sub2} {sub3}")
print(f"{sub1}: {lan}")
print(f"{sub2}: {eng}")
print(f"{sub3}: {math}")
print(f"총점: {total}")
print(f"평균: {average}")
"""
[실행 결과 예시] (입력: 85, 90, 78)
과목: 국어 영어 수학
국어: 85
영어: 90
수학: 78
총점: 253
평균: 84.33333333333333
"""
