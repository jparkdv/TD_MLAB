# 0025_list_sorting.py
# 목적: 리스트의 데이터를 정렬(sort)하고 순서를 반전(reverse)시키기
# -------------------------------------------------------
# Scenario:
# - 전시장에 전시될 '한국의 미' 사진 작품들의 파일명 리스트를 관리함.
# - 파일명들이 입력된 순서와 상관없이, 관람객이 보기 편하게 이름순으로 정렬함.
# - 때로는 강렬한 인상을 위해 순서를 완전히 거꾸로 뒤집어 배치하기도 함.
# -------------------------------------------------------

# 1. 사진 작품 리스트 생성
photo_works = ["Palace_05", "Hanja_Art", "Seoul_Night", "Kimchi_Texture", "Buddhism_Statue"]
print(f"초기 리스트: {photo_works}")

# 2. 알파벳순으로 정렬 (sort)
# 💡 sort는 리스트 자체를 순서대로 재배치합니다.
photo_works.sort()
print(f"알파벳 순서 정렬: {photo_works}")

# 3. 현재 순서를 반전 (reverse)
# 💡 reverse는 단순히 현재 상태에서 맨 뒤와 맨 앞을 바꿉니다.
photo_works.reverse()
print(f"알파벳 순서 반대 정렬: {photo_works}")

# 4. 정렬과 반전을 한 번에 (sort + reverse)
# 먼저 정렬한 다음, 그 결과를 반전시키면 알파벳 역순으로 정렬된 리스트가 됩니다.
photo_works.sort()  # 먼저 정렬
photo_works.reverse()  # 그 다음 반전
print(f"알파벳 역순 정렬: {photo_works}")

# 5. sortef() 함수를 사용한 정렬
# sorted()는 원본 리스트는 그대로 두고, 정렬된 새로운 리스트를 반환합니다.
sorted_works = sorted(photo_works)  # 원본은 그대로, 정렬된 새 리스트 생성
print(f"sorted()로 정렬된 새 리스트: {sorted_works}")
print(f"원본 리스트는 그대로: {photo_works}")