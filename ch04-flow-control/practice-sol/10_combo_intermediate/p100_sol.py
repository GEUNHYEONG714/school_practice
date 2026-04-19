"""
실습 100 풀이: 미니 인터프리터
"""
n = int(input())
x = 0  # 변수 x 초기값
y = 0  # 변수 y 초기값

for i in range(n):
    line = input()

    # 명령어 파싱 (공백 기준으로 분리)
    # PRINT는 2단어, SET/ADD는 3단어
    space1 = line.find(" ")
    cmd = line[:space1]

    if cmd == "PRINT":
        var_name = line[space1 + 1:]
        if var_name == "x":
            print(x)
        else:
            print(y)
    else:
        # SET 또는 ADD
        rest = line[space1 + 1:]
        space2 = rest.find(" ")
        var_name = rest[:space2]
        val = int(rest[space2 + 1:])

        if cmd == "SET":
            if var_name == "x":
                x = val
            else:
                y = val
        elif cmd == "ADD":
            if var_name == "x":
                x += val
            else:
                y += val
