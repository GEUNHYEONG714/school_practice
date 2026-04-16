"""
TITLE: 완전수 판별
DIFFICULTY: medium
TAGS: for, if, modulo

DESCRIPTION:
숫자를 입력받아 자기 자신을 제외한 약수의 합을 `N의 약수의 합: S` 형태로 출력한 뒤,
그 합이 자기 자신과 같으면 `N은(는) 완전수입니다!`, 아니면 `N은(는) 완전수가 아닙니다.`를 출력하시오.

예시:
- 입력: `6` → 출력: `6의 약수의 합: 6`, `6은(는) 완전수입니다!`
- 입력: `10` → 출력: `10의 약수의 합: 8`, `10은(는) 완전수가 아닙니다.`
"""
# META_TESTS:
# - stdin: "6"
#   expected_stdout: "6의 약수의 합: 6\n6은(는) 완전수입니다!"
# - stdin: "10"
#   expected_stdout: "10의 약수의 합: 8\n10은(는) 완전수가 아닙니다."
# - stdin: "28"
#   expected_stdout: "28의 약수의 합: 28\n28은(는) 완전수입니다!"

# 1부터 num-1까지의 약수의 합을 구해 비교
num = int(input())
total = 0
# TODO
