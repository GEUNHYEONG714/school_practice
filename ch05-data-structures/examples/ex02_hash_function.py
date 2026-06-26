# hash() — dict와 set이 빠른 진짜 이유
#
# hash(x) → 값을 고정된 정수로 변환하는 함수.
# 이 정수로 "어디에 저장할지" 한 번에 정해진다.

import os
import sys
import subprocess

if os.environ.get("PYTHONHASHSEED") != "42":
    os.environ["PYTHONHASHSEED"] = "42"
    sys.exit(subprocess.run([sys.executable] + sys.argv).returncode)

# --- 1. hash의 기본 특징 ---

# 같은 값 → 항상 같은 hash
print(hash("김민수") == hash("김민수"))   # True

# 다른 값 → 다른 hash (보통)
print(hash("김민수"))
print(hash("박서연"))

# 숫자, 문자열, 튜플은 hash 가능
print(hash(42))
print(hash((1, 2, 3)))

# list/dict/set은 내용이 바뀔 수 있어 hash 불가
# hash([1, 2])   # TypeError: unhashable type: 'list'


print()
# --- 2. 사물함 비유: hash로 저장 위치를 정한다 ---
# 사물함 100칸이 있다고 가정.
# hash(이름) % 100 → 들어갈 칸 번호

BUCKETS = 10000
lockers = [None] * BUCKETS

names = ["김민수", "박서연", "이준호", "최지우"]
for name in names:
    pos = hash(name) % BUCKETS
    lockers[pos] = name
    print(f"{name} → {pos}번 칸에 보관")


print()
# --- 3. 검색: 같은 계산으로 한 번에 찾는다 ---
target = "김민수"
pos = hash(target) % BUCKETS

print(f"'{target}' 찾기 → {pos}번 칸만 열어 보면 됨")
print(f"결과: {lockers[pos]}")

# list라면? 100칸을 처음부터 끝까지 모두 확인해야 한다.
# set/dict는 hash 덕분에 데이터가 아무리 많아져도
# "어디 보면 되는지"를 즉시 계산할 수 있다 → 그래서 빠르다.
