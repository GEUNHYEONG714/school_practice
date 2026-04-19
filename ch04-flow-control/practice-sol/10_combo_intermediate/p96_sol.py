"""
실습 96 풀이: 진수 덧셈기
"""
bin1 = input()
bin2 = input()

# 뒤에서부터 한 자리씩 덧셈
i = len(bin1) - 1  # bin1의 현재 위치
j = len(bin2) - 1  # bin2의 현재 위치
carry = 0
result = ""

while i >= 0 or j >= 0 or carry > 0:
    d1 = 0
    d2 = 0
    if i >= 0:
        if bin1[i] == "1":
            d1 = 1
        i -= 1
    if j >= 0:
        if bin2[j] == "1":
            d2 = 1
        j -= 1

    total = d1 + d2 + carry
    if total == 0:
        result = "0" + result
        carry = 0
    elif total == 1:
        result = "1" + result
        carry = 0
    elif total == 2:
        result = "0" + result
        carry = 1
    else:  # total == 3
        result = "1" + result
        carry = 1

# 앞의 불필요한 0 제거
while len(result) > 1 and result[0] == "0":
    result = result[1:]

print(result)
