# 0010_list_indexing.py (리스트 인덱싱)
# 목적: 다중 센서 데이터를 리스트(List) 구조로 통합 관리 및 인덱스 기반 조회 시스템 구현
# -------------------------------------------------------
# Scenario:
# - 분산되어 있는 개별 센서들을 하나의 하드웨어 리스트로 통합하여 관리 효율성을 높임.
# - 인덱싱(Indexing) 기술을 사용하여 특정 위치의 센서 상태를 선별적으로 호출함.
# - 시스템 내부에 연결된 전체 장비의 규모를 실시간으로 파악함.
#
# Requirements:
# - 4개의 센서 이름을 포함하는 리스트(hardware_list) 생성
# - 대괄호[]와 인덱스 번호를 활용한 특정 데이터 추출
# - len() 함수를 활용한 동적 리스트 길이(장비 총 개수) 계산 및 출력
# -------------------------------------------------------

# 1. 하드웨어 인벤토리 구축 (Hardware Inventory Setup)
# 전시장에 설치된 센서들의 명단을 하나의 리스트로 묶습니다.
hardware_list = ["motion", "temperature", "humidity", "door"]

# 2. 특정 센서 모니터링 (Selective Sensor Monitoring)
# 리스트의 시작은 1번이 아닌 0번임을 유의하여 특정 장비를 호출합니다.
print("Primary Sensor (Index 0):", hardware_list[0])   # 첫 번째 센서 호출
print("Tertiary Sensor (Index 2):", hardware_list[2])  # 세 번째 센서 호출

# 3. 시스템 현황 보고 (System Status Report)
# 전체 리스트 구성과 연결된 장비의 총 수량을 출력합니다.
print("Full Hardware List:", hardware_list)
print("Total Sensors Connected:", len(hardware_list))