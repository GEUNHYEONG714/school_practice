"""
TITLE: 로마 숫자 변환
DIFFICULTY: hard
TAGS: conversion, roman-numeral, while, if
EVAL: stdio

DESCRIPTION:
정수(1~3999)를 입력받아 로마 숫자로 변환하여 출력하세요.
- 로마 숫자 규칙:
  M=1000, CM=900, D=500, CD=400,
  C=100, XC=90, L=50, XL=40,
  X=10, IX=9, V=5, IV=4, I=1
- 큰 단위부터 차례로 빼면서 해당 로마 문자를 이어붙입니다.
- 리스트, 딕셔너리, 함수를 사용하지 마세요.

예시:
- 입력: `1994` → 출력: `MCMXCIV`
- 입력: `58` → 출력: `LVIII`
- 입력: `3999` → 출력: `MMMCMXCIX`
"""
# META_TESTS:
# - stdin: "1994"
#   expected_stdout: "MCMXCIV"
# - stdin: "58"
#   expected_stdout: "LVIII"
# - stdin: "3999"
#   expected_stdout: "MMMCMXCIX"

# 정수를 입력받아 로마 숫자로 변환하세요.
num = int(input())
# TODO
