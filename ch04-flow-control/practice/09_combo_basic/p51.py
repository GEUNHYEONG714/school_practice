"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 51: 학생 석차

5명의 점수를 입력받고, 특정 학생의 석차를 구합니다.
- 5명의 점수를 각각 변수에 저장
- 몇 번째 학생의 석차를 구할지 입력
- 해당 학생보다 점수가 높은 사람 수 + 1 = 석차

힌트: if문으로 각 학생 점수와 비교하여 석차를 계산합니다.
"""

# 아래에 석차 계산 코드를 작성하세요
print("=== 5명의 점수 입력 ===")
s1 = int(input("1번 학생 점수: "))
s2 = int(input("2번 학생 점수: "))
s3 = int(input("3번 학생 점수: "))
s4 = int(input("4번 학생 점수: "))
s5 = int(input("5번 학생 점수: "))

target = int(input("석차를 확인할 학생 번호 (1~5): "))

# 대상 학생의 점수 확인
if target == 1:
    score = s1
elif target == 2:
    score = s2
elif target == 3:
    score = s3
elif target == 4:
    score = s4
else:
    score = s5

# 석차 계산
rank = 1

if s1 > score:
    rank += 1

if s2 > score:
    rank += 1

if s3 > score:
    rank += 1

if s4 > score:
    rank += 1

if s5 > score:
    rank += 1

# 출력
print(f"{target}번 학생 점수: {score}")
print(f"석차: {rank}등")

"""
[실행 결과 예시]
=== 5명의 점수 입력 ===
1번 학생 점수: 85
2번 학생 점수: 92
3번 학생 점수: 78
4번 학생 점수: 95
5번 학생 점수: 88
석차를 확인할 학생 번호 (1~5): 1
1번 학생 점수: 85
석차: 4등
"""
