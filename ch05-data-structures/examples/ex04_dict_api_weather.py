# 실무 스타일 dict 예제 - REST API의 JSON을 파이썬 자료구조로 다루기
#
# 실무에서는 다른 서버(REST API)에 요청을 보내고,
# 서버는 보통 "JSON" 형식으로 데이터를 돌려준다.
# response.json()을 사용하면 JSON을 파이썬의 dict/list로 변환할 수 있다.
#   { "키": 값, "키": 값 }   ← JSON 객체는 파이썬 dict와 모양이 비슷하다.
#
# 이번 예제: 기상청 같은 날씨 서버(Open-Meteo)에서
#            "지금 서울 날씨"를 받아온 뒤 필요한 값만 골라 출력한다.
#   - API 키 불필요, 무료
#   - data["current"]처럼 키를 이용해 값을 꺼내는 연습

import requests   # pip install requests  (HTTP 요청을 보낼 때 많이 쓰는 라이브러리)

# --- 1. 요청할 주소와 조건(파라미터) 준비 ---
# 요청 조건은 dict로 정리해 params에 넘길 수 있다.
URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 37.5665,    # 서울시청 위도
    "longitude": 126.9780,  # 서울시청 경도
    "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m",
    "timezone": "Asia/Seoul",
}

# weather_code 숫자를 사람이 읽기 쉬운 한국어로 바꾸기 위한 dict
# 이런 "코드 -> 의미" 변환표도 dict의 대표적인 활용 예이다.
WEATHER_TEXT = {
    0: "맑음",
    1: "대체로 맑음",
    2: "부분적으로 흐림",
    3: "흐림",
    45: "안개",
    48: "서리 안개",
    51: "약한 이슬비",
    53: "이슬비",
    55: "강한 이슬비",
    61: "약한 비",
    63: "비",
    65: "강한 비",
    71: "약한 눈",
    73: "눈",
    75: "강한 눈",
    80: "약한 소나기",
    81: "소나기",
    82: "강한 소나기",
    95: "천둥번개",
}

# --- 2. 서버에 요청하고 JSON 받기 ---
try:
    response = requests.get(URL, params=params, timeout=10)
    data = response.json()   # JSON 응답을 파이썬 dict로 변환
except requests.RequestException:
    print("⚠ 인터넷 연결을 확인하세요. 날씨 서버에 접속하지 못했습니다.")
    raise SystemExit

# --- 3. 받아온 데이터 구조 확인 ---
print("받아온 데이터의 자료형:", type(data))   # <class 'dict'>
print("최상위 키 목록:", list(data.keys()))
print()

# --- 4. dict 안의 dict(중첩 dict)에서 값 꺼내기 ---
# data
#   └─ "current"        ← 현재 날씨 정보가 들어 있는 또 다른 dict
#         ├─ "temperature_2m": 20.6
#         ├─ "relative_humidity_2m": 94
#         └─ ...
current = data["current"]         # data["current"]는 그 자체가 dict
units = data["current_units"]     # 각 값의 단위(°C, % 등)도 dict로 들어 있다

temp = current["temperature_2m"]            # dict["키"] 로 값 꺼내기
feels = current["apparent_temperature"]
humidity = current["relative_humidity_2m"]
wind = current["wind_speed_10m"]
code = current["weather_code"]

# 날씨 코드 -> 한국어.
# 표에 없는 코드라면 dict.get의 기본값인 "정보 없음"을 사용한다.
sky = WEATHER_TEXT.get(code, "정보 없음")

# --- 5. 보기 좋게 출력 ---
print("=" * 32)
print("       지금 서울 날씨")
print("=" * 32)
print(f"  관측 시각 : {current['time']}")
print(f"  날      씨 : {sky}")
print(f"  기      온 : {temp}{units['temperature_2m']}")
print(f"  체  감  온 : {feels}{units['apparent_temperature']}")
print(f"  습      도 : {humidity}{units['relative_humidity_2m']}")
print(f"  풍      속 : {wind}{units['wind_speed_10m']}")
print("=" * 32)
