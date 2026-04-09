"""
실습 10 풀이: 3의 배수 건너뛰기
"""

# 1부터 20까지 반복
for i in range(1, 21):
    # 3의 배수이면 건너뛴다
    if i % 3 == 0:
        continue  # 아래 print를 실행하지 않고 다음 반복으로
    print(i)
