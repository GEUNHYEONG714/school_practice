"""
실습 101 풀이: 단어 검열기
"""

sentence = input("문장: ")
banned = input("금지어: ")

result = ""
i = 0
ban_len = len(banned)

while i < len(sentence):
    # 현재 위치에서 금지어 길이만큼 비교
    if sentence[i:i + ban_len] == banned:
        result += "***"
        i += ban_len  # 금지어 길이만큼 건너뜀
    else:
        result += sentence[i]
        i += 1

print(result)
