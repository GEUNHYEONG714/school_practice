"""
실습 57 풀이: 풍선 터뜨리기 (요세푸스)
"""

n, k = map(int, input("N K를 입력하세요: ").split())

# 비트마스크로 생존 관리 (비트 1~N 사용)
alive = 0
for i in range(1, n + 1):
    alive |= (1 << i)

result = ""
popped = 0      # 터뜨린 풍선 수
pos = 0         # 현재 위치 (0-based로 순회)
count = 0       # 카운트

while popped < n:
    pos += 1
    if pos > n:
        pos = 1

    # 생존한 풍선이면 카운트
    if alive & (1 << pos):
        count += 1
        if count == k:
            # K번째 풍선 터뜨리기
            alive &= ~(1 << pos)
            if popped > 0:
                result += " "
            result += str(pos)
            popped += 1
            count = 0

print(result)
