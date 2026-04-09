"""
실습 33 풀이: 문자열 길이 세기
"""

text = input("문자열을 입력하세요: ")
count = 0

# for문으로 한 글자씩 돌면서 카운트 증가
for char in text:
    count += 1

print("문자열 길이:", count)
