# 문제 4. 기능을 재사용하기 어렵다
#
# 함수는 '한 번 만들어 두면 어디서든 다시 쓰는 도구'다.
# 마치 우리가 print()나 len()을 가져다 쓰듯이!
# 중요한 점은 "코드를 짧게 만든다"가 전부가 아니라는 것이다.
# 함수는 잘 정리된 기능에 이름을 붙여, 다른 상황에서도 믿고 부를 수 있게 해 준다.

# --- 작은 도구 함수 두 개를 만든다 ---
def is_even(n):              # 숫자 하나를 받아 짝수인지 판단한다
    return n % 2 == 0

def rectangle_area(w, h):    # 가로와 세로를 받아 직사각형 넓이를 구한다
    return w * h


print("=" * 45)
print("1) 같은 함수를 여러 상황에서 다시 쓰기")
print("=" * 45)

# 한 번 만든 is_even()을 전혀 다른 상황들에서 그대로 재사용한다.
# 함수 안의 나머지 연산(n % 2 == 0)을 매번 다시 쓸 필요가 없다.
print("10은 짝수?", is_even(10))
print("7은 짝수?", is_even(7))

# 반복문 안에서도 그대로 불러 쓴다.
# "짝수 판별"이라는 작은 기능이 리스트 처리 코드 안에 자연스럽게 들어간다.
numbers = [3, 8, 15, 22, 41, 60]
evens = [n for n in numbers if is_even(n)]
print("짝수만 모으기:", evens)


print()
print("=" * 45)
print("2) 작은 함수를 '조립'해 큰 기능 만들기")
print("=" * 45)

# 방마다 넓이를 구해 집 전체 넓이를 계산한다.
# 작은 함수(rectangle_area)를 더 큰 함수(house_area)의 부품으로 사용한다.
def house_area(rooms):
    total = 0
    for w, h in rooms:
        total += rectangle_area(w, h)   # 작은 함수를 재사용
    return total

rooms = [(3, 4), (2, 2), (5, 3)]   # 각 방의 (가로, 세로)
print("거실 넓이   :", rectangle_area(3, 4))
print("집 전체 넓이:", house_area(rooms))

# --- 핵심 ---
#   - 한 번 잘 만든 함수는 복사할 필요 없이 '이름'으로 계속 불러 쓴다.
#   - 작은 함수들을 모아 더 큰 함수를 만든다.
#   - 잘 만든 함수는 다른 프로그램으로 가져가(import) 쓸 수도 있다.
#   - 그래서 함수는 "한 번 작성한 지식을 여러 곳에서 쓰는 방법"이다.
