# 0016_list_comparison.py (리스트 비교 및 조건 필터링 예제)
# 목적: 다중 리스트 비교 및 조건 필터링을 통한 카테고리별 장비 요약 시스템 구현
# -------------------------------------------------------
# Scenario:
# - 전시장에 설치된 전체 하드웨어(all_hardware) 중 '출력 장치' 카테고리에 속하는 것만 선별함.
# - 사전에 정의된 출력 장치 기준 리스트(output_devices)와 실시간 장비 목록을 대조함.
# - 카테고리에 포함되지 않는 장비(Sensor 등)는 별도로 보고하여 분류의 정확성을 높임.
# - 선별된 출력 장치들만 모아 관리자에게 최종 점검 리스트(found_outputs)를 제공함.
#
# Requirements:
# - 전체 장비 리스트 및 필터링 기준이 되는 카테고리 리스트 생성
# - for 문을 통한 전체 순회 및 'in' 연산자를 활용한 소속 여부 판별
# - 조건에 부합하는 항목을 새로운 리스트에 수집하고, 예외 케이스(else)에 대한 로그 출력
# - 최종 선별된 장비 목록 및 상세 데이터 보고
# -------------------------------------------------------

# 1. 데이터 베이스 및 기준 설정 (Data Foundation & Criteria)
all_hardware = ["Projector", "Speaker", "Sensor", "Monitor", "LED_Wall"]
output_devices = ["Projector", "Speaker", "Monitor", "LED_Wall"]
found_outputs = []

# 2. 카테고리 기반 자동 분류 루프 (Categorized Classification Loop)
for device in all_hardware:
    # 현재 장비가 '출력 장치' 기준 목록에 포함되는지 확인
    if device in output_devices:
        # 카테고리 일치 시 수집 리스트에 추가
        found_outputs.append(device)
    else:
        # 카테고리에 속하지 않는 경우 예외 로그 출력
        print(f"{device} is not an output device.")

# 3. 최종 분류 결과 보고 (Final Summary Report)
# 선별된 출력 장치들만 모인 최종 리스트를 출력합니다.
print("Found output devices:", found_outputs)