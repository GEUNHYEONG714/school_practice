"""
실습 47 풀이: 타자 연습
"""

# 연습 문장 (3문장을 순서대로 진행)
text1 = "Hello Python"
text2 = "I love coding"
text3 = "Practice makes perfect"

total_correct = 0  # 전체 맞은 글자
total_chars = 0    # 전체 글자 수
round_num = 1

print("=== 타자 연습 ===")
print("표시된 문장을 정확히 입력하세요!")
print()

# 3개의 문장에 대해 반복
while round_num <= 3:
    # 라운드별 원본 문장 선택
    if round_num == 1:
        original = text1
    elif round_num == 2:
        original = text2
    else:
        original = text3

    print("[" + str(round_num) + "번 문장] " + original)
    user_input = input("입력: ")

    # 글자별 비교
    correct = 0
    orig_len = len(original)
    input_len = len(user_input)

    # 짧은 쪽 길이까지 비교
    if orig_len < input_len:
        compare_len = orig_len
    else:
        compare_len = input_len

    i = 0
    while i < compare_len:
        if original[i] == user_input[i]:
            correct += 1
        i += 1

    # 정확도 계산 (원본 글자 수 기준)
    accuracy = correct * 100 / orig_len

    # 소수점 첫째 자리까지 출력 (수동 계산)
    accuracy_int = int(accuracy * 10) / 10

    print("정확도: " + str(accuracy_int) + "% (" + str(correct) + "/" + str(orig_len) + " 글자)")
    print()

    # 전체 누적
    total_correct += correct
    total_chars += orig_len

    round_num += 1

# 최종 결과
total_accuracy = total_correct * 100 / total_chars
total_accuracy_int = int(total_accuracy * 10) / 10

print("=== 최종 결과 ===")
print("전체 정확도: " + str(total_accuracy_int) + "% (" + str(total_correct) + "/" + str(total_chars) + " 글자)")
