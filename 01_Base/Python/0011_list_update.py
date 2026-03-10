# 0011_list_update.py (리스트 업데이트)
# 목적: 리스트의 추가·삭제·수정을 통한 실시간 장비 인벤토리 최신화 시스템 구현
# -------------------------------------------------------
# Scenario:
# - 전시장 운영 중 발생하는 장비의 고장, 신규 도입, 성능 업그레이드 상황을 관리함.
# - 고장 난 센서(Sensor)를 목록에서 영구 제외하여 운영 오류를 방지함.
# - 새로 도입된 레이저(Laser) 장비를 시스템 리스트에 등록함.
# - 기존 표준 프로젝터를 고해상도 장비(4K_Projector)로 교체하여 하드웨어 상태를 갱신함.
#
# Requirements:
# - 초기 장비 인벤토리 리스트 생성 및 초기화
# - .remove() 및 .append() 메소드를 활용한 리스트 요소의 동적 관리
# - 인덱스 참조(index[0])를 통한 특정 데이터의 직접 수정(Modify)
# - 최종 갱신된 리스트 정보 및 장비 총 수량(len) 출력
# -------------------------------------------------------

# 1. 초기 인벤토리 로드 (Initial Inventory Load)
inventory = ["Projector", "Speaker", "Sensor", "Laptop"]

# 2. 실시간 장비 변동 처리 (Real-time Asset Management)
# [삭제] 고장 난 장비를 목록에서 제거
inventory.remove("Sensor")

# [추가] 신규 도입 장비를 리스트 끝에 추가
inventory.append("Laser")

# [수정] 기존 노후 장비를 최신 장비로 업그레이드 (인덱스 0번 교체)
inventory[0] = "4K_Projector"

# 3. 최종 재고 현황 보고 (Final Asset Report)
# 최종 리스트 내용과 장비 수량을 출력하여 관리자에게 보고합니다.
print("Current Inventory List:", inventory)
print("Updated Inventory Count:", len(inventory))