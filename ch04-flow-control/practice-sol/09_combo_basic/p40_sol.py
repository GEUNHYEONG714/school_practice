"""
실습 40 풀이: 문자 빈도
"""

text = input("문자열을 입력하세요: ")

# 바깥 for: 각 글자를 하나씩 선택
for char in text:
    count = 0
    # 안쪽 for: 전체 문자열에서 해당 글자 개수 세기
    for c in text:
        if c == char:
            count += 1
    print(char + ": " + str(count) + "개")
