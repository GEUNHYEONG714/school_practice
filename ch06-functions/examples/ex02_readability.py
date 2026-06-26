# 문제 1. 코드가 길어져 이해하기 어렵다
#
# 온라인 주문의 '최종 결제금액'을 계산한다.
# (상품금액 합계 → 회원 할인 → 배송비 → 최종 금액)
# 함수가 없으면 이 흐름이 여러 계산식 사이에 묻힌다.
# 함수가 있으면 각 단계에 이름을 붙여 전체 흐름을 먼저 볼 수 있다.

prices = [12000, 8000, 23000]
is_member = True

print("=" * 45)
print("[함수 없이] 한 덩어리로 쭉 작성")
print("=" * 45)

# 무슨 일을 하는 코드일까?
# 지금은 짧아서 읽을 수 있지만, 계산 단계가 늘어나면 끝까지 따라가야만 흐름이 보인다.
subtotal = 0
for p in prices:
    subtotal += p

discount = 0
if is_member:
    discount = int(subtotal * 0.1)

paid = subtotal - discount

if paid >= 30000:
    shipping = 0
else:
    shipping = 3000

total = paid + shipping

print(f"상품합계: {subtotal}원")
print(f"할인    : {discount}원")
print(f"배송비  : {shipping}원")
print(f"최종금액: {total}원")


print()
print("=" * 45)
print("[함수 사용] 의미 단위로 이름을 붙인다")
print("=" * 45)

def calc_subtotal(prices):                # 상품금액 합계를 구하는 단계
    total = 0
    for p in prices:
        total += p
    return total

def calc_discount(subtotal, is_member):   # 회원 할인을 계산하는 단계
    if is_member:
        return int(subtotal * 0.1)
    return 0

def calc_shipping(amount):                # 배송비를 계산하는 단계 (3만원 이상 무료)
    if amount >= 30000:
        return 0
    return 3000

# 핵심 코드가 '요약'처럼 읽힌다.
# 먼저 큰 흐름을 보고, 세부 계산이 궁금할 때만 함수 안을 확인하면 된다.
subtotal = calc_subtotal(prices)
discount = calc_discount(subtotal, is_member)
paid = subtotal - discount
shipping = calc_shipping(paid)
total = paid + shipping

print(f"상품합계: {subtotal}원")
print(f"할인    : {discount}원")
print(f"배송비  : {shipping}원")
print(f"최종금액: {total}원")

# 함수 이름이 곧 '설명'이 된다:
#   calc_subtotal → 상품 합계를 구한다
#   calc_discount → 할인을 구한다
#   calc_shipping → 배송비를 구한다
# 좋은 함수 이름은 주석을 줄이고, 코드를 읽는 순서를 편하게 만든다.
