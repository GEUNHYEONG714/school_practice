"""
실습 풀이: 시험 합격
"""

written = int(input("필기 점수를 입력하세요: "))

# 바깥 if: 필기 합격 여부 확인
if written >= 60:
    print("필기 합격!")
    # 필기 합격일 때만 실기 점수를 입력받는다
    practical = int(input("실기 점수를 입력하세요: "))
    # 안쪽 if: 실기 합격 여부 확인
    if practical >= 70:
        print("최종 합격입니다!")
    else:
        print("실기 불합격입니다. 실기 재시험 대상입니다.")
else:
    print("필기 불합격입니다. 필기부터 다시 응시하세요.")
