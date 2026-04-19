"""
실습 68 풀이: 디지털 시계
"""

total_seconds = int(input("총 초를 입력하세요: "))

# 시, 분, 초 분리
h = total_seconds // 3600
m = (total_seconds % 3600) // 60
s = total_seconds % 60

# 2자리로 0 채워서 출력
print(str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))
