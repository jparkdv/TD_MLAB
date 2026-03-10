# 0027_tuple_operations.py (튜플의 연산과 데이터 통합)
# 목적: 튜플의 결합(+) 및 반복(*)을 활용한 통합 기술 데이터 세트 구축
# -------------------------------------------------------
# Scenario:
# - 전시 및 영화 프로젝트의 흩어진 기술 데이터를 하나로 통합함.
# - 규격 정보와 색상 정보를 합쳐 최종 송출용 마스터 패키지를 생성함.
# - 데이터의 포함 여부를 확인하여 시스템의 무결성을 검증함.
# -------------------------------------------------------

# 1. 기초 데이터 설정
resolution_info = (3840, 2160)
color_profile = ("Rec.709", "10-bit")

# 2. 튜플 결합 (Concatenation)
# 💡 두 튜플을 더하여(+) 하나의 큰 튜플로 통합하세요.
master_package = resolution_info + color_profile
print(f"1. Integrated Master Package: {master_package}")

# 3. 튜플 반복 (Repetition)
# 💡 테스트용 신호 (0, 255)를 3번 반복하여 튜플을 확장하세요.
test_signal = (0, 255)
repeated_signal = test_signal * 3
print(f"2. Repeated Test Signal: {repeated_signal}")

# 4. 데이터 검증 (Membership Check)
# 💡 'Rec.709'라는 값이 master_package 안에 들어있는지 확인(in)하세요.
# 결과는 True 또는 False로 출력됩니다.
is_correct_color = "Rec.709" in master_package
print(f"3. Color Profile Check: {is_correct_color}")

# 5. 데이터 개수 확인 (Length)
# 💡 master_package에 담긴 총 데이터 항목 개수를 출력하세요.
total_items = len(master_package)
print(f"4. Total metadata items: {total_items}")