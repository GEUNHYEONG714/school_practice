"""
실습 69 풀이: 봉우리 찾기
"""

n = int(input("N을 입력하세요: "))
nums = input("정수들을 입력하세요: ")

parts = nums.split()

if n == 1:
    print(1)
else:
    count = 0
    # 3개 값을 슬라이딩하며 비교
    prev = None
    curr = None
    idx = 0

    for p in parts:
        val = int(p)

        if idx == 0:
            # 첫 번째: 다음 값과만 비교하므로 일단 저장
            curr = val
        elif idx == 1:
            # 이제 이전 값의 봉우리 판별 가능 (첫 번째: 오른쪽만)
            if curr > val:
                count += 1
            prev = curr
            curr = val
        else:
            # 가운데 값 봉우리 판별
            if curr > prev and curr > val:
                count += 1
            prev = curr
            curr = val

        idx += 1

    # 마지막 원소: 왼쪽만 비교
    if curr > prev:
        count += 1

    print(count)
