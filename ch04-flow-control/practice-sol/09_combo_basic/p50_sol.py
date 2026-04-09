"""
실습 50 풀이: 별자리 운세
"""

month = int(input("생일 월을 입력하세요: "))
day = int(input("생일 일을 입력하세요: "))

# 별자리 판별
sign = ""

if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    sign = "물병자리"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    sign = "물고기자리"
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    sign = "양자리"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    sign = "황소자리"
elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    sign = "쌍둥이자리"
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    sign = "게자리"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    sign = "사자자리"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    sign = "처녀자리"
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    sign = "천칭자리"
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    sign = "전갈자리"
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    sign = "사수자리"
else:
    sign = "염소자리"

print("당신의 별자리는", sign + "입니다!")

# 별자리별 운세 출력
if sign == "물병자리":
    print("오늘의 운세: 창의적인 아이디어가 떠오르는 날이에요!")
elif sign == "물고기자리":
    print("오늘의 운세: 감성이 풍부해지는 하루입니다!")
elif sign == "양자리":
    print("오늘의 운세: 도전하면 좋은 결과가 있어요!")
elif sign == "황소자리":
    print("오늘의 운세: 꾸준한 노력이 빛을 발해요!")
elif sign == "쌍둥이자리":
    print("오늘의 운세: 소통이 활발해지는 날이에요!")
elif sign == "게자리":
    print("오늘의 운세: 새로운 만남이 기다리고 있어요!")
elif sign == "사자자리":
    print("오늘의 운세: 리더십을 발휘할 기회가 와요!")
elif sign == "처녀자리":
    print("오늘의 운세: 꼼꼼함이 행운을 가져다줘요!")
elif sign == "천칭자리":
    print("오늘의 운세: 균형 잡힌 판단이 중요한 날이에요!")
elif sign == "전갈자리":
    print("오늘의 운세: 자신감을 가지면 좋은 일이 생겨요!")
elif sign == "사수자리":
    print("오늘의 운세: 모험을 즐기면 행운이 따라와요!")
else:
    print("오늘의 운세: 성실함이 큰 보상을 가져다줘요!")
