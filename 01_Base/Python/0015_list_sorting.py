# 0015_list_sorting.py (리스트 정렬)
# 목적: 리스트 정렬(Sort) 및 역순(Reverse) 기능을 활용한 데이터 구조화
# -------------------------------------------------------
# Scenario:
# - 전시장 장비 리스트를 관리 효율성을 위해 알파벳순으로 자동 정렬함.
# - 필요에 따라 최신 등록 순서나 특정 기준의 역순으로 리스트를 뒤집어 확인함.
# - 정렬된 데이터를 통해 관리자가 장비 현황을 한눈에 파악할 수 있도록 시각화함.
#
# Requirements:
# - 다중 장비 명칭을 포함하는 원본 리스트(my_gear) 생성
# - .sort() 메소드를 활용한 오름차순(알파벳순) 정렬 실행
# - .reverse() 메소드를 활용한 현재 리스트 순서 반전 기능 구현
# - 각 단계별 정렬 결과물 출력 및 데이터 무결성 확인
# -------------------------------------------------------

# 1. 원본 데이터 로드 (Initial Data Load)
my_gear = ["Projector", "Camera", "Sensor", "Audio", "Laptop"]

# 2. 알파벳순 정렬 프로세스 (Alphabetical Sorting)
# .sort()는 리스트 자체를 알파벳 순서(A-Z)로 영구 정렬합니다.
my_gear.sort()
print("Sorted Inventory (A-Z):", my_gear)

# 3. 데이터 순서 반전 프로세스 (Reverse Order)
# .reverse()는 현재 리스트의 순서를 앞뒤로 뒤집습니다.
my_gear.reverse()
print("Reversed Inventory (Z-A):", my_gear)

# 4. 최종 데이터 확정 보고 (Final Verification) 
print("Inventory organization complete.")