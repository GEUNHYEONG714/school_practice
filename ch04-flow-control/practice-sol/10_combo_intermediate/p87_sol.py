"""
실습 87 풀이: 로마 숫자 변환
"""
num = int(input())
result = ""

# M = 1000
while num >= 1000:
    result += "M"
    num -= 1000

# CM = 900
while num >= 900:
    result += "CM"
    num -= 900

# D = 500
while num >= 500:
    result += "D"
    num -= 500

# CD = 400
while num >= 400:
    result += "CD"
    num -= 400

# C = 100
while num >= 100:
    result += "C"
    num -= 100

# XC = 90
while num >= 90:
    result += "XC"
    num -= 90

# L = 50
while num >= 50:
    result += "L"
    num -= 50

# XL = 40
while num >= 40:
    result += "XL"
    num -= 40

# X = 10
while num >= 10:
    result += "X"
    num -= 10

# IX = 9
while num >= 9:
    result += "IX"
    num -= 9

# V = 5
while num >= 5:
    result += "V"
    num -= 5

# IV = 4
while num >= 4:
    result += "IV"
    num -= 4

# I = 1
while num >= 1:
    result += "I"
    num -= 1

print(result)
