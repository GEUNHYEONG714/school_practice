"""
실습 12 풀이: 특정 문자 찾기
"""

text = "hello python"
target = "p"
found = False  # 찾았는지 여부를 기록

# 문자열을 한 글자씩 순회하며 위치도 함께 추적
for i in range(len(text)):
    if text[i] == target:
        print("'" + target + "'을(를) " + str(i) + "번째 위치에서 찾았습니다!")
        found = True
        break  # 처음 찾은 위치에서 즉시 종료

# 끝까지 찾지 못한 경우
if not found:
    print("찾지 못했습니다")
