# [실무] 진짜 OPEN API 호출 → JSON 파싱 → 화면 출력
#
# 인터넷의 공개 API(Open-Meteo, 회원가입·API키 불필요)에서
# 현재 날씨를 받아와 화면에 보여 준다.
#
# 핵심 흐름:  요청 → JSON 응답 → 파이썬 dict로 변환 → 안에서 값 꺼내기
#   - API가 돌려주는 JSON은 파이썬의 dict / list / 숫자 / 문자열과 1:1로 대응된다.
#   - 그래서 JSON을 파싱하면 우리가 배운 "중첩 자료구조"가 그대로 나온다.

import json
import urllib.request
import urllib.parse

# --- 1. 요청할 도시 (이름 → 좌표 tuple) ---
# 값이 (위도, 경도) 튜플인 dict. 좌표는 바뀌면 안 되니 tuple이 어울린다.
CITIES = {
    "서울": (37.5665, 126.9780),
    "부산": (35.1796, 129.0756),
    "제주": (33.4996, 126.5312),
}

# 날씨 코드(WMO) → 한글 설명. (API는 숫자만 주므로 우리가 말로 바꿔 준다)
WEATHER_TEXT = {
    0: "맑음", 1: "대체로 맑음", 2: "구름 조금", 3: "흐림",
    45: "안개", 48: "짙은 안개",
    51: "약한 이슬비", 61: "약한 비", 63: "비", 65: "강한 비",
    71: "약한 눈", 73: "눈", 75: "강한 눈",
    80: "소나기", 95: "천둥번개",
}


def fetch_weather(lat, lng):
    """좌표를 받아 Open-Meteo에 요청하고, 응답 JSON을 dict로 돌려준다."""
    base = "https://api.open-meteo.com/v1/forecast"
    # 쿼리 파라미터도 dict로 구성하면 깔끔하다.
    params = {
        "latitude": lat,
        "longitude": lng,
        "current_weather": "true",
        "timezone": "Asia/Seoul",
    }
    url = base + "?" + urllib.parse.urlencode(params)

    with urllib.request.urlopen(url, timeout=10) as resp:
        raw = resp.read().decode("utf-8")   # 응답은 글자(JSON 문자열)

    # 핵심! JSON 문자열 → 파이썬 dict 로 변환
    return json.loads(raw)


# 네트워크가 안 될 때를 대비한 예비 데이터 (실제 응답과 같은 모양)
SAMPLE = {
    "current_weather": {
        "temperature": 28.7, "windspeed": 6.5,
        "winddirection": 267, "weathercode": 0, "is_day": 1,
    }
}


# --- 2. 도시별로 날씨 받아서 출력 ---
print("=== 지금 날씨 (Open-Meteo) ===\n")

for name, coords in CITIES.items():
    lat, lng = coords                       # 튜플 언패킹
    try:
        data = fetch_weather(lat, lng)
    except Exception as e:
        # 인터넷이 막혀도 수업이 멈추지 않도록 예비 데이터 사용
        print(f"[{name}] API 호출 실패({e.__class__.__name__}) → 예시 데이터로 대체")
        data = SAMPLE

    # --- 3. 중첩 dict에서 값 꺼내기 ---
    # data["current_weather"]는 또 다른 dict → 그 안에서 [키]로 꺼낸다.
    cw = data["current_weather"]
    temp = cw["temperature"]
    wind = cw["windspeed"]
    code = cw["weathercode"]

    # 숫자 코드를 한글로 (없는 코드면 기본값) → dict.get() 의 방어적 사용
    sky = WEATHER_TEXT.get(code, "알 수 없음")
    day = "낮" if cw["is_day"] == 1 else "밤"

    print(f"[{name}] {sky}  🌡 {temp}°C  💨 {wind} km/h  ({day})")


print()
# --- 4. 핵심 정리 ---
# - json.loads(문자열) → dict 로 바꾸면, API 응답을 우리가 배운 dict처럼 다룰 수 있다.
# - 응답은 보통 dict 안에 dict/list가 중첩돼 있다 → [키]·[인덱스]를 이어 붙여 접근.
# - 외부 데이터는 키가 없거나 호출이 실패할 수 있다 → .get()과 try/except로 방어한다.
# - 숫자 코드를 사람이 읽을 말로 바꾸는 "변환표"도 dict로 만들면 깔끔하다.
