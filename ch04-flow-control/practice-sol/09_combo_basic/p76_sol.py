"""
실습 76 풀이: 문자열 압축 (Run-Length Encoding)
"""

s = input("문자열을 입력하세요: ")
result = ""

# 첫 문자와 카운트 초기화
current = s[0]
count = 1

# 두 번째 문자부터 순회
for i in range(1, len(s)):
    if s[i] == current:
        # 같은 문자가 연속되면 카운트 증가
        count += 1
    else:
        # 다른 문자가 나오면 이전 문자와 카운트를 결과에 추가
        result += current + str(count)
        current = s[i]
        count = 1

# 마지막 문자 처리
result += current + str(count)

print(result)
