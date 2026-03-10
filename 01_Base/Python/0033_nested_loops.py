# 0033_nested_loops.py (중첩 반복문 기초)
# 목적: 리스트 내부의 리스트를 순회하며 다차원 데이터를 체계적으로 출력하기
# -------------------------------------------------------
# Scenario:
# - 전시관별 작품 리스트를 관리함.
# - 각 전시홀(Hall A, Hall B)을 순회하며 내부에 배치된 작품명을 하나씩 추출함.
# -------------------------------------------------------

# 1. 중첩 리스트 데이터 (전시장 구조)
# [홀 이름, [작품1, 작품2, 작품3]] 형태의 리스트들을 담은 큰 리스트입니다.
exhibition_data = [
    ["Hall A", ["The Core", "Light Wave", "Mirror Study"]],
    ["Hall B", ["Seoul Night", "Tradition Flow"]]
]

# 2. 중첩 반복문 실행
# 💡 바깥쪽 반복문: 각 홀의 정보(리스트)를 하나씩 가져옵니다.
for hall_info in exhibition_data:
    hall_name = hall_info[0]
    artworks = hall_info[1]
    
    print(f"\n--- {hall_name} 리스트 ---")
    
    # 💡 안쪽 반복문: 선택된 홀의 작품 리스트(artworks)에서 작품을 하나씩 꺼냅니다.
    for artwork in artworks:
        print(f"작품명: {artwork}")

# 3. 추가 미션 (심화)
# 모든 작품의 총 개수를 카운트하는 변수를 만들고 마지막에 출력해보세요.
total_count = 0
for hall_info in exhibition_data:
    for work in hall_info[1]:
        total_count += 1

print(f"\n총 전시 작품 수: {total_count}개")