"""
실습 98 풀이: 숫자 한글 변환기
"""

num = int(input("숫자(1~9999): "))

result = ""

# 천의 자리
d = num // 1000
if d > 0:
    if d == 1:
        result += "천"
    else:
        # 숫자를 한글로 변환
        if d == 2:
            result += "이천"
        elif d == 3:
            result += "삼천"
        elif d == 4:
            result += "사천"
        elif d == 5:
            result += "오천"
        elif d == 6:
            result += "육천"
        elif d == 7:
            result += "칠천"
        elif d == 8:
            result += "팔천"
        elif d == 9:
            result += "구천"

# 백의 자리
d = (num % 1000) // 100
if d > 0:
    if d == 1:
        result += "백"
    elif d == 2:
        result += "이백"
    elif d == 3:
        result += "삼백"
    elif d == 4:
        result += "사백"
    elif d == 5:
        result += "오백"
    elif d == 6:
        result += "육백"
    elif d == 7:
        result += "칠백"
    elif d == 8:
        result += "팔백"
    elif d == 9:
        result += "구백"

# 십의 자리
d = (num % 100) // 10
if d > 0:
    if d == 1:
        result += "십"
    elif d == 2:
        result += "이십"
    elif d == 3:
        result += "삼십"
    elif d == 4:
        result += "사십"
    elif d == 5:
        result += "오십"
    elif d == 6:
        result += "육십"
    elif d == 7:
        result += "칠십"
    elif d == 8:
        result += "팔십"
    elif d == 9:
        result += "구십"

# 일의 자리
d = num % 10
if d > 0:
    if d == 1:
        result += "일"
    elif d == 2:
        result += "이"
    elif d == 3:
        result += "삼"
    elif d == 4:
        result += "사"
    elif d == 5:
        result += "오"
    elif d == 6:
        result += "육"
    elif d == 7:
        result += "칠"
    elif d == 8:
        result += "팔"
    elif d == 9:
        result += "구"

print(result)
