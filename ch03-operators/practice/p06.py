"""
실습 6: 시간 변환

초(seconds)를 입력받아 시, 분, 초로 변환하여 출력하세요.

힌트: //(몫)과 %(나머지)를 사용합니다.
      1시간 = 3600초, 1분 = 60초
"""

seconds = int(input("초를 입력하세요: "))

# 아래에 시, 분, 초로 변환하여 출력하세요

# 초 출력
print(str(seconds) + "초")

# 시간, 분, 초 계산 후 출력
time = seconds // 3600
minute = seconds % 3600 // 60
second = seconds % 60
print(f"= {time}시간 {minute}분 {second}초")

"""
[실행 결과 예시] (입력: 3725)
3725초
= 1시간 2분 5초
"""
