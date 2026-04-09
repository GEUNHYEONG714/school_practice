"""
실습 풀이: 알파벳 삼각형
"""

n = int(input("줄 수를 입력하세요: "))

# 바깥 for문: 줄 번호 (1 ~ n)
for i in range(1, n + 1):
    # 안쪽 for문: 각 줄에 A부터 i번째 알파벳까지 출력
    # chr(65) = 'A', chr(66) = 'B', ...
    for j in range(i):
        print(chr(65 + j), end="")
    print()  # 줄바꿈
