"""
실습 6 풀이: 별 한 줄 출력
"""

n = int(input("별의 개수를 입력하세요: "))

# end=""를 사용하면 print() 후 줄바꿈하지 않는다
for i in range(n):
    print("*", end="")

# 별 출력이 끝난 후 줄바꿈
print()
