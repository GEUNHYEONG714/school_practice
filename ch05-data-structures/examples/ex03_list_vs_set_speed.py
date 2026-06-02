# 리스트 vs 집합(set) — hash의 위력을 "시간"으로 체감하기
#
# 같은 데이터를 list와 set에 똑같이 담고,
# "이 값이 있나?"를 검색하는 데 걸리는 시간을 비교한다.
#
#   list : 앞에서부터 하나씩 전부 확인  → 데이터가 N개면 최대 N번  (느림)
#   set  : hash로 위치를 즉시 계산      → 데이터가 몇 개든 한 번에  (빠름)

import time

# --- 데이터 크기 ---
# 참고: 10억(1_000_000_000)개는 메모리가 수십 GB 필요해서 보통 PC에서는 불가능하다.
#       (리스트만 8GB+, 정수 객체까지 합하면 28GB+ → MemoryError)
#       1천만이면 차이를 충분히 체감할 수 있다. 더 키우려면 N 값만 바꾸면 된다.
N = 10_000_000          # 데이터 개수: 1천만
SEARCH_COUNT = 100      # 검색을 몇 번 반복할지 (시간 차이를 키우기 위해)

print(f"데이터 {N:,}개를 list와 set에 담는 중...")
data_list = list(range(N))
data_set = set(data_list)
print("준비 완료!\n")

# 일부러 "없는 값"(-1)을 찾는다.
# → list는 끝까지 다 뒤져야 하는 최악의 경우가 된다.
target = -1

# --- 1. list에서 검색 (O(N): 처음부터 끝까지 확인) ---
start = time.perf_counter()
for _ in range(SEARCH_COUNT):
    found = target in data_list
list_time = time.perf_counter() - start

# --- 2. set에서 검색 (O(1): hash로 위치 계산 후 즉시 확인) ---
start = time.perf_counter()
for _ in range(SEARCH_COUNT):
    found = target in data_set
set_time = time.perf_counter() - start

# --- 3. 결과 비교 ---
print(f"데이터 {N:,}개에서 검색을 {SEARCH_COUNT}번 반복한 시간")
print(f"  list : {list_time:8.4f}초")
print(f"  set  : {set_time:8.4f}초")
print(f"\n→ set이 약 {list_time / max(set_time, 1e-9):,.0f}배 빠르다!")


# --- 4. 데이터가 커질수록 차이가 벌어진다 ---
# 핵심: 데이터를 10배로 늘리면
#   list 검색 시간도 ≈ 10배로 늘어나지만 (느려짐)
#   set 검색 시간은 거의 그대로다 (데이터 양과 무관!)
print("\n" + "=" * 58)
print("데이터를 키워가며 비교 (없는 값을 20번씩 검색)")
print("=" * 58)
print(f"{'데이터 개수':>12} | {'list':>11} | {'set':>11} | {'배수':>10}")
print("-" * 58)

for n in [10_000, 100_000, 1_000_000, 10_000_000]:
    lst = list(range(n))
    st = set(lst)
    reps = 20

    start = time.perf_counter()
    for _ in range(reps):
        -1 in lst
    lt = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(reps):
        -1 in st
    stime = time.perf_counter() - start

    print(f"{n:>12,} | {lt:>9.5f}초 | {stime:>9.6f}초 | {lt / max(stime, 1e-9):>8,.0f}배")

print("-" * 58)
print("list: 데이터가 10배 → 시간도 약 10배 (한 줄씩 다 뒤지니까)")
print("set : 데이터가 10배 → 시간 그대로 (hash로 한 번에 찾으니까)")
