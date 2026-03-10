# 0012_list_slicing.py (리스트 슬라이싱)
# 목적: 리스트 슬라이싱(Slicing) 및 멤버십 연산자(in)를 활용한 선별적 데이터 검수 시스템 구현
# -------------------------------------------------------
# Scenario:
# - 전시장 내 수많은 센서를 효율적으로 관리하기 위해 구역별/기능별로 데이터를 분할함.
# - 리스트의 전반부(Quick Check)와 후반부(Precision Check)를 분리하여 단계별 점검을 수행함.
# - 특정 핵심 센서(Smoke)의 존재 여부를 실시간으로 파악하여 안전 프로토콜 가동 준비를 마침.
#
# Requirements:
# - 다중 센서 데이터를 포함하는 통합 리스트(all_sensors) 생성
# - 슬라이싱 연산자[:]를 활용한 범위 기반 데이터 추출 (처음 3개 및 마지막 2개)
# - 'in' 연산자를 활용한 특정 요소의 포함 여부 조건문 설계
# - 추출된 하위 리스트 및 검색 결과의 시각적 출력
# -------------------------------------------------------

# 1. 통합 센서 데이터 로드 (Full Sensor Data Load)
all_sensors = ["Motion", "Flame", "Smoke", "CO2", "Lidar", "Camera"]

# 2. 선별적 구역 점검 (Sectional Inspection)
# [슬라이싱] 처음 3개의 센서 추출 (Index 0, 1, 2)
quick_check = all_sensors[:3]

# [슬라이싱] 마지막 2개의 센서 추출 (뒤에서부터 2개)
precision_check = all_sensors[-2:]

# 3. 핵심 장비 탐지 및 보고 (Key Device Detection)
# 'in' 연산자를 사용하여 화재 감지 센서의 연결 상태를 즉시 확인
if "Smoke" in all_sensors:
    print("Fire Safety Sensor Detected.")

# 4. 최종 점검 결과 출력 (Final Audit Output)
print("Quick Check Group (A-Zone):", quick_check)
print("Precision Check Group (B-Zone):", precision_check)