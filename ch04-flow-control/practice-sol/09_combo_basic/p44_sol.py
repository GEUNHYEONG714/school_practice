"""
실습 44 풀이: 출석부
"""

n = int(input("학생 수를 입력하세요: "))
present = 0  # 출석 인원
absent = 0   # 결석 인원

for i in range(1, n + 1):
    # 이름 입력
    name = input(str(i) + "번 학생 이름: ")

    # 출석 여부 입력
    status = int(input("출석 여부 (1:출석 / 0:결석): "))

    # 출석/결석 카운트
    if status == 1:
        print(name, "- 출석")
        present += 1
    else:
        print(name, "- 결석")
        absent += 1

print("--- 출석 결과 ---")
print("출석:", present, "명")
print("결석:", absent, "명")
