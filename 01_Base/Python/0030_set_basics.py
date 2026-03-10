# 0030_set_basics.py (집합 기초와 중복 제거)
# 목적: 집합(Set)의 특성을 활용하여 데이터의 유일성 확보하기
# -------------------------------------------------------
# Scenario:
# - 전시 작품들에 붙은 수많은 태그 중 중복을 제거한 고유 목록을 추출함.
# - 새로운 전시 테마를 추가하거나 기존 테마를 안전하게 삭제함.
# - 집합의 '중복 불허' 성질을 이용해 데이터 리스트를 정제함.
# -------------------------------------------------------

# 1. 중복된 데이터가 포함된 태그 리스트
raw_tags = ["Landscape", "Portrait", "Cityscape", "Landscape", "Abstract", "Portrait"]
print(f"1. 원본 태그 리스트: {raw_tags}")

# 2. 리스트를 집합으로 변환하여 중복 제거 (Set Conversion)
# 💡 set() 함수를 사용하면 중복된 "Landscape"와 "Portrait"가 하나만 남습니다.
unique_tags = set(raw_tags)
print(f"2. 중복 제거된 고유 태그: {unique_tags}")

# 3. 새로운 태그 추가 (Add)
# 💡 집합에 "Nightview"라는 새로운 테마를 추가해보세요.
unique_tags.add("Nightview")

# 4. 특정 태그 삭제 (Remove)
# 💡 "Abstract" 테마를 목록에서 삭제해보세요.
unique_tags.remove("Abstract")
print(f"3. 편집 후 태그 목록: {unique_tags}")

# 5. 데이터 존재 여부 확인 (Membership Check)
# 💡 "Landscape"가 현재 태그 목록에 있는지 확인해보세요.
has_landscape = "Landscape" in unique_tags
print(f"4. Landscape 포함 여부: {has_landscape}")