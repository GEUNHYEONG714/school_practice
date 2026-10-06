"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 71: 연속 같은 문자

문자열을 입력받아 같은 문자가 연속으로 가장 많이 반복된 횟수를 출력합니다.

예시:
- aabbcccaa → 'c'가 3번 연속 → 3
- abcd → 모두 1번 → 1

힌트: for 반복문으로 문자열을 순회하며 이전 문자와 비교합니다.
      현재 연속 횟수와 최대 연속 횟수를 각각 관리합니다.
"""

s = input("문자열을 입력하세요: ")

# 아래에 코드를 작성하세요
count = 1
max_count = 1

for i in range(1, len(s)):
    # 이전 문자와 같은지 확인
    if s[i] == s[i - 1]:
        count += 1
    else:
        count = 1

    # 최대 연속 횟수 갱신
    if count > max_count:
        max_count = count

# 출력
print(max_count)

"""
[실행 결과 예시] (입력: aabbcccaa)
3
"""
