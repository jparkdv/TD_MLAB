# 0031_set_operations.py (집합 연산과 데이터 분석)
# 목적: 합집합, 교집합, 차집합을 활용하여 서로 다른 데이터 세트 비교하기
# -------------------------------------------------------
# Scenario:
# - 두 개의 전시 섹션(City, Tradition)에 사용된 태그 목록을 비교 분석함.
# - 두 섹션의 공통 키워드와 고유 키워드를 추출하여 전시 가이드를 제작함.
# -------------------------------------------------------

# 1. 두 섹션의 태그 집합 설정
tags_city = {"Night", "Seoul", "Building", "Light"}
tags_tradition = {"Old", "Seoul", "Hanbok", "Light"}

# 2. 교집합 (Intersection)
# 💡 두 곳 모두에 있는 공통 태그를 찾으세요. (기호: &)
common_tags = tags_city & tags_tradition   
print(f"1. 공통 키워드: {common_tags}")

# 3. 합집합 (Union)
# 💡 두 섹션의 모든 태그를 합친 전체 목록을 만드세요. (기호: |)
all_tags = tags_city | tags_tradition
print(f"2. 전체 키워드 목록: {all_tags}")

# 4. 차집합 (Difference)
# 💡 tags_city에는 있지만 tags_tradition에는 없는 도시 섹션만의 키워드를 찾으세요. (기호: -)
city_only = tags_city - tags_tradition
print(f"3. 도시 섹션 고유 키워드: {city_only}")