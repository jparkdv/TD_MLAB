# 0029_dict_methods.py (딕셔너리 메서드 활용)
# 목적: 딕셔너리 전용 메서드를 활용한 데이터 추출 및 안전한 접근 기술 습득
# -------------------------------------------------------
# Scenario:
# - 전시 자산 관리 시스템에서 특정 작품의 상세 스펙을 일괄 조회함.
# - 시스템 운영 중 발생할 수 있는 데이터 누락(Missing Key)에 대비한 안전 장치를 마련함.
# -------------------------------------------------------

# 1. 초기 자산 데이터 설정
asset_info = {
    "id": "PHOTO_001",
    "title": "Seoul Night",
    "resolution": "4K",
    "status": "Archived"
}

# 2. 키(Key) 목록만 가져오기
# 💡 모든 정보의 이름표들만 리스트 형태로 확인합니다.
info_keys = asset_info.keys()
print(f"1. Available Metadata Keys: {info_keys}")

# 3. 값(Value) 목록만 가져오기
# 💡 이름표는 떼고 실제 데이터들만 모아서 확인합니다.
info_values = asset_info.values()
print(f"2. Actual Data Values: {info_values}")

# 4. 키와 값의 쌍(Item) 가져오기
# 💡 (키, 값) 형태의 튜플 쌍으로 묶인 목록을 가져옵니다.
info_items = asset_info.items()
print(f"3. All Metadata Items: {info_items}")

# 5. 안전한 데이터 접근 (The .get() Method)
# 💡 존재하지 않는 키를 호출할 때 []를 쓰면 에러가 나지만, .get()은 None을 반환합니다.
# 'location'이라는 정보는 현재 딕셔너리에 없지만, 에러 없이 가져와보세요.
location = asset_info.get("location")
print(f"4. Asset Location: {location}") 

# 💡 정보가 없을 때 출력될 '기본값'을 직접 설정할 수도 있습니다.
location_with_default = asset_info.get("location", "Unknown Location")
print(f"5. Asset Location (Safe): {location_with_default}")

# -------------------------------------------------------
# 0029_2_dict_practice.py (직접 타이핑해보기!)
my_gear = {"mic": "Shure SM7B", "interface": "Apollo Solo"}

# 1. '이름표' 목록만 출력해보세요 (.keys 활용)
print(my_gear.keys())

# 2. '내용물' 목록만 출력해보세요 (.values 활용)
print(my_gear.values())

# 3. 'speaker'가 있는지 찾아보되, 없으면 "No Speaker"라고 나오게 하세요 (.get 활용)
print(my_gear.get("speaker", "No Speaker"))