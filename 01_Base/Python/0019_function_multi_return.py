# 0019_function_multi_return.py (함수 다중 반환값)
# 목적: 쉼표(,)를 활용하여 함수에서 여러 개의 결과값을 동시에 반환받기
# -------------------------------------------------------
# Scenario:
# - 미디어 아트 전시장의 프로젝터와 서버 장비는 온습도에 매우 민감함.
# - 환경 감지 시스템에서 '온도(Temperature)'와 '습도(Humidity)' 데이터를 동시에 읽어와야 함.
# - 하나의 함수가 두 개의 중요한 데이터를 한 번에 반환(return)하도록 설계함.
# - 반환된 두 데이터를 각각의 변수에 나누어 담아 최종 모니터링 메시지를 출력함.
# -------------------------------------------------------

# 1. 환경 측정 엔진 정의 (Environment Sensor Engine)
def get_room_condition():
    # 센서가 측정한 가상의 온습도 데이터
    temp = 22
    humidity = 55
    
    # 💡 핵심: 두 개의 결과값을 쉼표로 연결하여 한 번에 반환합니다.
    return temp, humidity

# 2. 시스템 가동 및 결과값 수집 (Data Unpacking)
# 함수가 던져준 두 개의 값(22, 55)을 순서대로 current_temp와 current_humidity에 나누어 담습니다.
current_temp, current_humidity = get_room_condition()

# 3. 최종 결과 출력 (Status Report)
print(f"[환경 점검] 현재 전시장의 온도는 {current_temp}°C, 습도는 {current_humidity}% 입니다.")